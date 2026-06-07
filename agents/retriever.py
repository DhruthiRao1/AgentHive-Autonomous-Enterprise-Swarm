def retrieve(ticket):

    if "vpn" in ticket.lower():
        return "VPN troubleshooting knowledge article"

    if "outlook" in ticket.lower():
        return "Outlook repair knowledge article"

    if "password" in ticket.lower():
        return "Password reset procedure"

    return "General IT support knowledge article"
