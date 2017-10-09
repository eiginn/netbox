from __future__ import unicode_literals


# IP address families
AF_CHOICES = (
    (4, 'IPv4'),
    (6, 'IPv6'),
)

# Prefix statuses
PREFIX_STATUS_CONTAINER = 0
PREFIX_STATUS_ACTIVE = 1
PREFIX_STATUS_RESERVED = 2
PREFIX_STATUS_DEPRECATED = 3
PREFIX_STATUS_CHOICES = (
    (PREFIX_STATUS_CONTAINER, 'Container'),
    (PREFIX_STATUS_ACTIVE, 'Active'),
    (PREFIX_STATUS_RESERVED, 'Reserved'),
    (PREFIX_STATUS_DEPRECATED, 'Deprecated')
)

# IP address statuses
IPADDRESS_STATUS_ACTIVE = 1
IPADDRESS_STATUS_RESERVED = 2
IPADDRESS_STATUS_DEPRECATED = 3
IPADDRESS_STATUS_DHCP = 5
IPADDRESS_STATUS_CHOICES = (
    (IPADDRESS_STATUS_ACTIVE, 'Active'),
    (IPADDRESS_STATUS_RESERVED, 'Reserved'),
    (IPADDRESS_STATUS_DEPRECATED, 'Deprecated'),
    (IPADDRESS_STATUS_DHCP, 'DHCP')
)

# IP address roles
IPADDRESS_ROLE_LOOPBACK = 10
IPADDRESS_ROLE_SECONDARY = 20
IPADDRESS_ROLE_ANYCAST = 30
IPADDRESS_ROLE_VIP = 40
IPADDRESS_ROLE_VRRP = 41
IPADDRESS_ROLE_HSRP = 42
IPADDRESS_ROLE_GLBP = 43
IPADDRESS_ROLE_CARP = 44
IPADDRESS_ROLE_CHOICES = (
    (IPADDRESS_ROLE_LOOPBACK, 'Loopback'),
    (IPADDRESS_ROLE_SECONDARY, 'Secondary'),
    (IPADDRESS_ROLE_ANYCAST, 'Anycast'),
    (IPADDRESS_ROLE_VIP, 'VIP'),
    (IPADDRESS_ROLE_VRRP, 'VRRP'),
    (IPADDRESS_ROLE_HSRP, 'HSRP'),
    (IPADDRESS_ROLE_GLBP, 'GLBP'),
    (IPADDRESS_ROLE_CARP, 'CARP'),
)

# VLAN statuses
VLAN_STATUS_ACTIVE = 1
VLAN_STATUS_RESERVED = 2
VLAN_STATUS_DEPRECATED = 3
VLAN_STATUS_CHOICES = (
    (VLAN_STATUS_ACTIVE, 'Active'),
    (VLAN_STATUS_RESERVED, 'Reserved'),
    (VLAN_STATUS_DEPRECATED, 'Deprecated')
)

# Bootstrap CSS classes for various statuses
STATUS_CHOICE_CLASSES = {
    0: 'default',
    1: 'primary',
    2: 'info',
    3: 'danger',
    4: 'warning',
    5: 'success',
}

# IP protocols (for services)
IP_PROTOCOL_TCP = 6
IP_PROTOCOL_UDP = 17
IP_PROTOCOL_CHOICES = (
    (IP_PROTOCOL_TCP, 'TCP'),
    (IP_PROTOCOL_UDP, 'UDP'),
)
