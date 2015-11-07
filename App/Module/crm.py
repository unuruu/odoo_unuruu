# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2009-2014 Monos Group (<http://monos.mn>).
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

from openerp.osv import fields, osv
from openerp.tools import float_round, float_repr
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
from openerp import api, _
from lxml import etree
import openerp.addons.decimal_precision as dp
import time

class hr_analytic_issue(osv.osv):
    _inherit = 'hr.analytic.timesheet'
    _description = 'HR Analytic Timesheet'
    
    _columns = {
        'lead_id' : fields.many2one('crm.lead', 'Lead'),
    }
    
class crm_lead(osv.osv):
    _inherit = 'crm.lead'
    
    _columns = {  
        'timesheet_ids': fields.one2many('hr.analytic.timesheet', 'lead_id', 'Timesheets'),
    }