TABLE_MAPPING = {
    "SYSMAC": {
        "query": """
            SELECT 
                acc_master.code,
                acc_master.name,
                acc_master.opening_balance,
                acc_master.debit,
                acc_master.credit,
                acc_master.place,
                acc_master.phone2,
                acc_departments.department AS openingdepartment
            FROM acc_master
            LEFT JOIN acc_departments ON acc_master.openingdepartment = acc_departments.department_id
            WHERE acc_master.super_code = 'DEBTO'
        """
    },
    "SYSMAC LEDGERS": {
        "query": """
            SELECT
                acc_ledgers.code,
                acc_ledgers.particulars,
                acc_ledgers.debit,
                acc_ledgers.credit,
                acc_ledgers.entry_mode,
                acc_ledgers."date" AS entry_date,
                CAST(acc_ledgers.voucher_no AS INTEGER) AS voucher_no,
                acc_ledgers.narration
            FROM acc_ledgers
            LEFT JOIN acc_master ON acc_ledgers.code = acc_master.code
            WHERE acc_master.super_code = 'DEBTO';
        """
    },
    "IMCB LLP": {
        "query": """
            SELECT 
                acc_master.code,
                acc_master.name,
                acc_master.opening_balance,
                acc_master.debit,
                acc_master.credit,
                acc_master.place,
                acc_master.phone2,
                acc_departments.department AS openingdepartment
            FROM acc_master
            LEFT JOIN acc_departments ON acc_master.openingdepartment = acc_departments.department_id
            WHERE acc_master.super_code = 'DEBTO'
        """
    },
    "IMC LLP LEDGERS": {
        "query": """
            SELECT
                acc_ledgers.code,
                acc_ledgers.particulars,
                acc_ledgers.debit,
                acc_ledgers.credit,
                acc_ledgers.entry_mode,
                acc_ledgers."date" AS entry_date,
                CAST(acc_ledgers.voucher_no AS INTEGER) AS voucher_no,
                acc_ledgers.narration
            FROM acc_ledgers
            LEFT JOIN acc_master ON acc_ledgers.code = acc_master.code
            WHERE acc_master.super_code = 'DEBTO';
        """
    },
    "IMC": {
        "query": """
            SELECT 
                acc_master.code,
                acc_master.name,
                acc_master.opening_balance,
                acc_master.debit,
                acc_master.credit,
                acc_master.place,
                acc_master.phone2,
                acc_departments.department AS openingdepartment
            FROM acc_master
            LEFT JOIN acc_departments ON acc_master.openingdepartment = acc_departments.department_id
            WHERE acc_master.super_code = 'DEBTO'
        """
    },
    "IMC LEDGERS": {
        "query": """
            SELECT
                acc_ledgers.code,
                acc_ledgers.particulars,
                acc_ledgers.debit,
                acc_ledgers.credit,
                acc_ledgers.entry_mode,
                acc_ledgers."date" AS entry_date,
                CAST(acc_ledgers.voucher_no AS INTEGER) AS voucher_no,
                acc_ledgers.narration
            FROM acc_ledgers
            LEFT JOIN acc_master ON acc_ledgers.code = acc_master.code
            WHERE acc_master.super_code = 'DEBTO';
        """
    },
    "Sysmac_INFO": {
        "query": """
            SELECT 
                acc_master.code,
                acc_master.name,
                acc_master.opening_balance,
                acc_master.debit,
                acc_master.credit,
                acc_master.place,
                acc_master.phone2,
                acc_departments.department AS openingdepartment
            FROM acc_master
            LEFT JOIN acc_departments ON acc_master.openingdepartment = acc_departments.department_id
            WHERE acc_master.super_code = 'DEBTO'
        """
    },
    "Sysmac_INFO LEDGERS": {
        "query": """
            SELECT
                acc_ledgers.code,
                acc_ledgers.particulars,
                acc_ledgers.debit,
                acc_ledgers.credit,
                acc_ledgers.entry_mode,
                acc_ledgers."date" AS entry_date,
                CAST(acc_ledgers.voucher_no AS INTEGER) AS voucher_no,
                acc_ledgers.narration
            FROM acc_ledgers
            LEFT JOIN acc_master ON acc_ledgers.code = acc_master.code
            WHERE acc_master.super_code = 'DEBTO';
        """
    },
    "DQ": {
        "query": """
            SELECT 
                acc_master.code,
                acc_master.name,
                acc_master.opening_balance,
                acc_master.debit,
                acc_master.credit,
                acc_master.place,
                acc_master.phone2,
                acc_departments.department AS openingdepartment
            FROM acc_master
            LEFT JOIN acc_departments ON acc_master.openingdepartment = acc_departments.department_id
            WHERE acc_master.super_code = 'DEBTO'
        """
    },
    "DQ LEDGERS": {
        "query": """
            SELECT
                acc_ledgers.code,
                acc_ledgers.particulars,
                acc_ledgers.debit,
                acc_ledgers.credit,
                acc_ledgers.entry_mode,
                acc_ledgers."date" AS entry_date,
                CAST(acc_ledgers.voucher_no AS INTEGER) AS voucher_no,
                acc_ledgers.narration
            FROM acc_ledgers
            LEFT JOIN acc_master ON acc_ledgers.code = acc_master.code
            WHERE acc_master.super_code = 'DEBTO';
        """
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
        """
    }
}
