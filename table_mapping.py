TABLE_MAPPING = {
    "IMC": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code IN ('IMCC', 'IMCDI', 'IMK', 'IMM', 'RC', 'SYSK')"
    },
    "IMCB": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "Sysmac_INFO": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "DQ": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "SYSMAC": {
        "table": "acc_master",
        "columns": "code, name, opening_balance, debit, credit, place, phone2, openingdepartment",
        "condition": "super_code = 'DEBTO'"
    },
    "RRC_CLIENTS": {
        "query": """
            SELECT 
              rrc_clients.code,
              rrc_clients.name,
              rrc_clients.address,
              rrc_clients.branch,
              rrc_clients.district,
              rrc_clients.state,
              rrc_product.name AS software,
              rrc_clients.mobile,
              rrc_clients.installationdate,
              rrc_clients.priorty,
              rrc_clients.directdealing,
              rrc_clients.rout,
              rrc_clients.amc,
              rrc_clients.amcamt,
              rrc_clients.accountcode,
              rrc_clients.address3,
              rrc_clients.lictype,
              rrc_clients.clients,
              rrc_clients.sp,
              rrc_clients.nature
            FROM rrc_clients
            LEFT JOIN rrc_product ON rrc_clients.software = rrc_product.code
            WHERE rrc_clients.directdealing IN ('Y','S')
        """
    }
}
