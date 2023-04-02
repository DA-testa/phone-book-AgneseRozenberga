# python3
#Agnese Rozenberga 221RDB117 11.grupa
class Query:
    def __init__(self, query):
        self.type, self.number = query[0], int(query[1])
        if self.type == 'add': self.name = query[2]

def read_queries():
    n = int(input()) ; return [Query(input().split()) for i in range(n)]

def write_responses(result): print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    # Keep list of all existing (i.e. not deleted yet) contacts.
    for cur_query in queries:
        if cur_query.type == 'add': contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del': 
            if cur_query.number in contacts: del contacts[cur_query.number]
        else: response = contacts.get(cur_query.number, 'not found'); result.append(response)
    return result

if __name__ == '__main__': 
    write_responses(process_queries(read_queries()))
