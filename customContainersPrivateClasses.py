class TagCloud:
    def __init__(self):
        self.__tags = {}
    
    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) + 1
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(),0)
    def __setitem__ (self, tag, count):
        self.__tags[tag.lower()] = count
    def __len__(self):
        return len(self.__tags)
    def __iter__(self):
        return iter(self.__tags)
cloud = TagCloud()
cloud["python"]
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.__tags)

"""BUT WHAT IF..."""

print(cloud.__tags["Pythons"])
#This will crash with the above code normally WITHOUT __tags (instead of
# self.tags).
#This private function is less about security and more about a warning
cloud.__dict__
#^gives a key to access directly