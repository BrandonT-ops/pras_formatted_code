""" Imports for Data Manager """
import json

class Data_manager():
    """ Model to manage data in the entire project """
    def __init__(self):
        """ Initialising the class but well we dont know his attributes yet... """

    def data_encrypter(self):
        """ Function to encrypt data """

    def data_decrypter(self):
        """ Function to decrypt data """
    
          

class Json_manager(Data_manager):
    """ This is a specialisation of Data manager who manages JSONs """
    def __init__(self, file_name, data, file_path):
        """ Initialising JSON Manager attributes """
        self.file_name = file_name
        self.data = data
        self.file_path = file_path
        super().__init__(self)
        
    def check_if_file_exists(self):
        """ function to check if JSON file exists """
        ans = os.path.exists(self.file_path)
        return ans

    def json_read_from_file(self):
        """ function to read JSON from file and return a dictionary"""
        #read from file and return dictionary
        try:
            with open('JSON/'+ self.file_name) as json_file:
                data = json.load(json_file)
        except:
            print("Error: "+ self.file_name + " Absent ")	
            data = {}
		
        return data


    def json_write_to_file(self):
        """ function to write JSON to file and returns true if succeeded or false if failed"""
        ans = False
	    #convert dictionary to json String
        json_string = json.dumps(self.data, indent = 4, sort_keys = True)
	
        try:
		    #write to file
            with open('JSON/'+ self.file_name, 'w') as outfile:
                outfile.write(json_string)
                ans = True
        except:
            ans = False

        return ans


class File_manager(Data_manager):
    """ This is a specialisation of Data manager which manages Text Files """
    def __init__(self, file_path):
        """ Initialising File manager """
        self.file_path = file_path
        super().__init__(self)


    def check_if_file_exists(self):
        """ function to check if the file exists """
        ans = os.path.exists(self.file_path)
        return ans

    def read_from_file(self, indicator):
        """ function to read from text file """
        f= open(self.file_path, 'r')
        while True:
            try:
                line=next(f)
			#if we find the indicator, the next line is the needed information
                if (line == str(indicator)+"\n"):
                    return next(f)
            except StopIteration:
                break
        f.close()

    def write_to_file(self, content, indicator):
        """ function to write to text file""" 
        f = open(self.file_path, "r+")
        lines = f.readlines()
        count = 0
        for line in lines:
            if line == indicator+"\n":
                lines[count+1] = content
                break
            count = count + 1
        f.close()

        f1 = open(self.file_path, "w")
        for newLine in lines:
            f1.write(newLine)
        f1.close