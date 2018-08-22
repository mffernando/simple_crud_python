from DML import db_insert, db_update, db_delete, db_select
from pprint import pprint

#new users
#db_insert('user4', '1234-1234', 'user4@email.com')
#db_insert('user5', '1234-1234', 'user5@email.com')
#db_insert('user6', '1234-1234', 'user6@email.com')
#db_insert('user7', '1234-1234', 'user7@email.com')
#pprint(db_insert('user8', '1234,1234', 'user8@email.com'))
#db_insert('user9', '1234', 'user9@email.com')
#db_insert('user10', '1234', 'user10@email.com')

#list users
pprint(db_select('1234', 'phone'))
