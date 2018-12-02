
{
    'name': "Exercise-odoo",
    'summary': """Manage trainings""",
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    'demo': [
        'demo.xml',
    ],
}