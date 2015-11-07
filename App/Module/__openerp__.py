# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2009-2015 Asterisk Technologies LLC (<http://asterisk-tech.mn/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'CRM Timesheet',
    'version': '1.0',
    'category': 'CRM',
    'description': """
CRM Additional Features
===============================================================================================
Adds the feature to write timesheet line on CRM lead and opportunity.

-----------------------------------------------------------------------------------------------

    """,
    'author': 'Asterisk Technologies LLC',
    'depends': ['crm'],
    'website': 'http://www.asterisk-tech.mn',
    'data': [
        'crm_view.xml'
    ],
    'price': 30,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
