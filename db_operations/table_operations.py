# flake8: noqa: F401

def get_tables_info(connection, schema):
    query = """
    SELECT 
        TABLE_NAME table_name, 
        TABLE_COMMENT table_comment
    FROM 
        INFORMATION_SCHEMA.TABLES
    WHERE 
        TABLE_SCHEMA = %s;
    """
    return connection.execute_query(query, (schema, ))


def get_table_columns(connection, schema, table_name):
    query = """
    SELECT 
        c.COLUMN_NAME column_name, 
        c.COLUMN_TYPE column_type, 
        c.CHARACTER_MAXIMUM_LENGTH column_length,
        CASE WHEN k.COLUMN_NAME IS NOT NULL THEN 'YES' ELSE 'NO' END AS is_primary,
        c.IS_NULLABLE is_nullable,
        c.COLUMN_DEFAULT column_default,
        c.COLUMN_COMMENT column_comment
    FROM 
        INFORMATION_SCHEMA.COLUMNS c
    LEFT JOIN 
        INFORMATION_SCHEMA.KEY_COLUMN_USAGE k
    ON 
        c.TABLE_SCHEMA = k.TABLE_SCHEMA 
        AND c.TABLE_NAME = k.TABLE_NAME 
        AND c.COLUMN_NAME = k.COLUMN_NAME 
        AND k.CONSTRAINT_NAME = 'PRIMARY'
    WHERE 
        c.TABLE_SCHEMA = %s 
        AND c.TABLE_NAME = %s
    ORDER BY 
        c.ORDINAL_POSITION;
    """
    return connection.execute_query(query, (schema, table_name))


def get_table_indexes(connection, schema, table_name):
    query = """
    SELECT 
        INDEX_NAME index_name,
        GROUP_CONCAT(COLUMN_NAME ORDER BY SEQ_IN_INDEX) column_name,
        CASE NON_UNIQUE
            WHEN 0 THEN 'YES'
            ELSE 'NO'
        END AS is_unique,
        INDEX_TYPE index_type,
        INDEX_COMMENT index_comment
    FROM 
        INFORMATION_SCHEMA.STATISTICS
    WHERE 
        TABLE_SCHEMA = %s 
        AND TABLE_NAME = %s
    GROUP BY 
        INDEX_NAME, NON_UNIQUE, INDEX_TYPE, INDEX_COMMENT;
    """
    return connection.execute_query(query, (schema, table_name))
