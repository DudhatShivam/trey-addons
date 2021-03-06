# -*- coding: utf-8 -*-
###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2018-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
###############################################################################
{
    'name': 'Juniper Booking WebService Import',
    'category': 'Bookings System',
    'summary': 'Juniper Booking WebService',
    'version': '8.0.1.0.0',
    'description': '''
        This module import Juniper bookings from a xml file
    ''',
    'author': 'Trey (www.trey.es)',
    'depends': [
        'booking_webservice_juniper',
        'booking_webservice_methabook',
    ],
    'data': [
        'views/webservice_view.xml',
        'wizard/wizard_manual_update.xml',
        'wizard/wizard_assing_partner_account_ref.xml',
        'wizard/wizard_cancel_juniper_booking.xml',
    ],
    'external_dependencies': {
        'python': ['xmltodict', 'xlrd'],
    },
    'installable': True,
}
