from py2neo import Graph, Node, Relationship
import os

jp_graph_url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')

username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

jp_graph = Graph(jp_graph_url)# + '/db/jp/', username=username, password=password)

class Word(Node):

    def find(word):
        word_node = jp_graph.find_one('Word', 'word', word)
        return word_node

    def __init__(self, word):
        self.word = word #Node("Word", word=word)
        self.properties = Word.find(word)#Node("Word", word=word)
        #self.properties = Node("Word", word=word).walk()
        #print(dir(Node("Word", word=word)))

    def __str__(self):
        #print(Word.find(self.word))
        return "{word}".format(word=self.word)#wdir=(Node("Word",word=self.word))



    def get_kanji_in_word(self, word):
        query = '''
        MATCH (kanji:Kanji)-[:IN]->(word:Word)
        WHERE word.word = {word}
        RETURN kanji
        ORDER BY kanji.average
        '''
        return jp_graph.run(query, word=self.word)
