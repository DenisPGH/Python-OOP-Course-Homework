"""Upon initialization the class Storage will not receive any parameters.
 It should have 3 instance attributes: categories (empty list), topics (empty list),
 documents (empty list). The class should have the following methods:"""
from test.category import Category
from test.document import Document
from test.topic import Topic


class Storage:
    def __init__(self):
        self.categories=[]
        self.topics=[]
        self.documents=[]
    @staticmethod
    def __return_object_by_id(id,lists):
        for each in lists:
            if id==each.id:
                return each

    def add_category(self,category:Category): # - add the category if it is not in the list
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic:Topic): # - add the topic if it does not exist
        if topic not in self.topics:
            self.topics.append(topic)

    def	add_document(self,document:Document) : #- add the document if it does not exist
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id: int, new_name:str):
        # - edit the name of the category with the provided id
        searched_category=Storage.__return_object_by_id(category_id,self.categories)
        searched_category.name=new_name

    def edit_topic(self,topic_id: int, new_topic: str, new_storage_folder: str):
        # - edit the topic with the given id
        searched_topic=Storage.__return_object_by_id(topic_id,self.topics)
        searched_topic.topic=new_topic
        searched_topic.storage_folder=new_storage_folder

    def	edit_document(self,document_id: int, new_file_name: str): # - edit the document with the given id
        searched_document=Storage.__return_object_by_id(document_id,self.documents)
        searched_document.file_name=new_file_name

    def delete_category(self,category_id): # - delete the category with the provided id
        cat_for_del=Storage.__return_object_by_id(category_id,self.categories)
        self.categories.remove(cat_for_del)

    #•	delete_topic(topic_id) - delete the topic with the provided id
    def delete_topic(self,topic_id): # - delete the category with the provided id
        topic_for_del=Storage.__return_object_by_id(topic_id,self.topics)
        self.topics.remove(topic_for_del)

    # •	delete_document(document_id) - delete the document with the provided id
    def delete_document(self,document_id): # - delete the category with the provided id
        docu_for_del=Storage.__return_object_by_id(document_id,self.documents)
        self.documents.remove(docu_for_del)

    def get_document(self,document_id): # - return the document with the provided id
        get_docu=Storage.__return_object_by_id(document_id,self.documents)
        return get_docu

    def __repr__(self) : #- returns a string representation of each document on separate lines
        result=""
        for each_docu in self.documents:
            result+=f"{each_docu}\n"

        return result


