"""Technician scheduling, published as an MCP server.

Owned by FieldPro, the vendor Summit Wireless pays for field-service scheduling.
You would never see this code in real life; you'd only get a command or a URL.
"""
from fastmcp import FastMCP

mcp = FastMCP("Field Service")

# Stand-in for the vendor's scheduling database.
APPOINTMENTS = {
    "APT-2291": {
        "customer": "Ludwig",
        "postal_code": "83440",
        "window": "Tomorrow, 8:00-10:00 AM",
        "fee": "$79",
        "status": "booked",
    },
}


@mcp.tool
def find_appointments(customer: str) -> list[dict]:
    """Find technician appointments for a customer by first name."""
    return [
        {"appointment_id": appointment_id, **details}
        for appointment_id, details in APPOINTMENTS.items()
        if details["customer"].lower() == customer.lower()
    ]


@mcp.tool
def cancel_appointment(appointment_id: str, reason: str) -> str:
    """Cancel a technician appointment and waive its fee. Give the customer-facing reason."""
    appointment = APPOINTMENTS.get(appointment_id)
    if appointment is None:
        return f"No appointment with id {appointment_id}."
    appointment["status"] = "cancelled"
    appointment["fee"] = "$0 (waived)"
    return f"Cancelled {appointment_id} and waived the fee. Reason: {reason}"


if __name__ == "__main__":
    mcp.run()
