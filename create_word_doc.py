from word_doc_generator import create_table_word_document, save_document
from db_handler import get_database_connection
from db_operations.table_operations import get_tables_info, get_table_columns, get_table_indexes

if __name__ == "__main__":
    # 获取数据库连接
    connection = get_database_connection()
    if connection.connect():
        try:
            result = {"tables": [], "tableInfos": []}
            # 返回获取的数据
            schema = 'infi_dev_s1'  # 请自行修改为您的数据库 schema
            tables = get_tables_info(connection, schema)

            for table in tables:
                table_name = table['table_name']
                table_comment = table['table_comment']
                result['tables'].append({
                    "tableName": table_name,
                    "tableComment": table_comment
                })

                tableInfos = {
                    "tableName": table_name,
                    "tableComment": table_comment,
                    "tableColumns": [],
                    "tableIndexs": [],
                }
                # 获取表字段信息
                columns = get_table_columns(connection, schema, table_name)

                for column in columns:
                    tableInfos['tableColumns'].append({
                        "columnName":
                        column["column_name"],
                        "columnType":
                        column["column_type"],
                        "columnLength":
                        column["column_length"],
                        "isPrimary":
                        column["is_primary"],
                        "isNullable":
                        column["is_nullable"],
                        "columnDefault":
                        column["column_default"],
                        "columnComment":
                        column["column_comment"],
                    })

                # 获取表索引信息
                indexs = get_table_indexes(connection, schema, table_name)

                for index in indexs:
                    tableInfos['tableIndexs'].append({
                        "indexName":
                        index['index_name'],
                        "columnName":
                        index['column_name'],
                        "isUnique":
                        index['is_unique'],
                        "indexType":
                        index['index_type'],
                        "indexComment":
                        index['index_comment'],
                    })
                result['tableInfos'].append(tableInfos)
            # 生成Word文档
            doc = create_table_word_document(result)
            saved_filename = save_document(doc)
            print(f"文档已生成并保存为: {saved_filename}")
        except Exception as e:
            print(f"生成文档时发生错误: {str(e)}")
        finally:
            connection.disconnect()  # 关闭数据库连接
    else:
        print("无法连接到数据库")
