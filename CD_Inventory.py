#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes and OOP
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Larkin, 2021-Aug-30, added code for functionality
#------------------------------------------#
# -- DATA -- #
import pickle
import os

strFileName = 'cdInventory.dat'
lstOfCDObjects = []
intChoice = None

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        cd_added:function that adds a new CD to 
        __str__: (string) outputs string displaying stored CD data

    """
    # TOdone Add Code to the CD class
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        '''Initializes private variables for cd_id, cd_title, and cd_artist'''
        # -- attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    # -- Properties -- #
    @property
    def cd_id(self):
        '''sets __cd_id'''
        return self.__cd_id
    
    @property
    def cd_title(self):
        '''sets __cd_title'''
        return self.__cd_title
    
    @property
    def cd_artist(self):
        '''sets __cd_artist'''
        return self.__cd_artist
    
    @cd_id.setter
    def cd_id(self, value):
        '''gets __cd_id'''
        boolean = True
        while boolean:
            try:
                self.__cd_id = int(value)
                boolean = False
            except ValueError:
                print('CD ID must be an integer.')
    
    @cd_title.setter
    def cd_title(self, value):
        '''gets __cd_title'''
        self.__cd_artist = value
    
    @cd_artist.setter
    def cd_artist(self, value):
        '''gets __cd_artist'''
        self.__cd_artist = value
        


    # -- Methods -- #
    
    def cd_added(self, lstObj):
        '''Function to add new cd to existing list
        Args:
            lstObj: (list of objects) List to append new cd to
        Returns:
            sorted_lstObj: (list of objects) new updated and sorted cd list'''
        cd_data = {'ID': self.__cd_id, 'Title': self.__cd_title, 'Artist': self.__cd_artist}
        lstObj.append(cd_data)
        sorted_lstObj = sorted(lstObj, key = lambda i: i['ID'])
        return sorted_lstObj
    
    def compare_ID(self, lstObj):
        '''Function to compare new cd to existing list
        Args:
            lstObj: (List of Dics) List of CDs to compare to
        Returns:
            self.__cd_id: (Integer) New CD ID
        '''
        boolean = True
        for row in lstObj:
            if self.__cd_id == row['ID']:
                while boolean:
                    try:
                        self.__cd_id = int(input('This ID is already in use, please input another.'))
                        boolean = False
                    except ValueError:
                        print('The CD ID must have a numerical value.')
        return self.__cd_id

    def __str__(self):
        '''Method to output data read into CD class'''
        return '{} |\t{} (by: {})'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
    
    

    
# -- PROCESSING -- #
class FileIO():
    """Processes data to and from file:

    properties:
        None
        
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
    """

    # TOdone Add code to process data from a file
    def read_file(file):
        '''reads data from file for program use
        Args: 
            file (data file): file to read data from
        Returns:
            data (list of dics): data read from the file
        '''
        try:
            with open(file, 'rb') as f:
                data = pickle.load(f)
            return data
        
        except FileNotFoundError:
            with open(file, 'xb'):
                data = True
            return data
    
    # TOdone Add code to process data to a file
    def write_file(file, lstObj):
        '''writes data to file from program
        Args:
            file (data file): file to write function to
            lstObj (list of dics): data to write to file
        Returns:
            None
        '''
        with open(file, 'wb') as f:
            pickle.dump(lstObj, f)
    
    def delete_file(file):
        '''Funciton to delte file
        Args:
            File: (string) Name of data file to delete
        Returns:
            None
            '''
        os.remove(file)


# -- PRESENTATION (Input/Output) -- #
class IO:
    # TOdone add docstring
    '''Displays data, and accepts user inputs and outputs:
        
        properties:
            None
        
        methods:
            display_menu: prints menu
            user_choice: gets and stores user's choice for selecting choice
            display_inventory: prints current CD inventory
            cd_input: gets and stores input for a CD's ID, Title, and Artist
        '''
    # TOdone add code to show menu to user
    @staticmethod
    def display_menu():
        '''Function to display menu
        Args:
            None
        Returns:
            None
            '''
        print('\nSelect one of the following options:\n\n',
              '\t1: Display Current Inventory\n',
              '\t2: Add New CD to Inventory\n',
              '\t3: Save Current Inventory to File\n',
              '\t4: Load Saved Inventory from File\n',
              '\t5: Exit the CD Inventory Program')
        
    # TOdone add code to captures user's choice
    @staticmethod
    def user_choice():
        '''Function to captures user's choice for menu
        Args: 
            None
        Returns:
            choice: (integer) stores user's choice
        '''
        choice = ''
        while choice not in [1, 2, 3, 4, 5]:
            try:
                choice = int(input('Please enter the number corresponding to your choice.\n\t'))
            except ValueError:
                print('Please enter a numerical value.')
        return choice
    
    # TOdone add code to display the current data on screen
    @staticmethod
    def display_inventory(lstObj):
        '''Function to display current CD inventory
        Args:
            lstObj: (List of Dictionaries) List information is displayed from
        Returns:
            None
        '''
        print('\n======= The Current Inventory =======\n')
        print('   ID |\tCD Title (by: Artist)\n')
        for row in lstObj:
            print('\t{} |\t{} (by: {})'.format(*row.values()))
        print('\n=====================================\n')
    
    # TOdone add code to get CD data from user
    @staticmethod
    def cd_input():
        '''Function to gather information about a new CD
        Args:
            None
        Returns:
            newID: (integer) User input new ID
            newTitle: (string) User input title
            newArtist: (string) User input artist
        '''
        boolean = True
        while boolean:
            try: 
                newID = int(input('What is the CD\'s ID number?   ').strip())
                boolean = False
            except ValueError:
                print('The CD ID must be a number.')
        newTitle = input('What is the CD\'s title?   ').strip()
        newArtist = input('What is the artist\'s name?   ').strip()
        return newID, newTitle, newArtist
    
    @staticmethod
    def new_inventory_menu(file):
        '''Funciton to display menu upon creaion of new CD Inventory
        Args:
            File: (string) Name of data file created
        Returns:
            None
        '''
        print('\nThe file \''+ file +'\' has just been created.',
          '\n\nThe CD Inventory is Empty!', 
          '\n\nPlease select one of the following choices to continue:',
          '\n\t2: Add New CD to Inventory'
          '\n\t5: Exit the CD Inventory Program')
        
    @staticmethod
    def reload_choice():
        '''Function to gather user choice for reloading options
        Args:
            None
        Returns:
            rld_choice: (integer) user's menu choice
        '''
        boolean = True
        while boolean:
            try: 
                rld_choice = int(input('All unsaved data will be lost after reload.' + 
                       ' Select one of the following choices: \n\t1: To Continue WITHOUT Saving' +
                       '\n\t2: To Save AND Continue' + 
                       '\nOr any other number to return to the main menu.\n\t'))
                boolean = False
            except ValueError:
                print('Please enter a numerical value.')
        return rld_choice
    
    @staticmethod
    def exit_choice():
        '''Function to gather user choice for exiting program
        Args:
            None
        Returns:
            exit_yn
        '''
        exit_yn = input('If you exit now, all unsaved data will be lost.'+
                   '\nEnter \'y\' to continue, or enter any other value to return to main menu.\n\t').lower()
        return exit_yn
# -- Main Body of Script -- #
# TOdone Add Code to the main body

# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.read_file(strFileName)

if lstOfCDObjects == True:
    IO.new_inventory_menu(strFileName)

# Display menu to user
while intChoice != 5:
    if lstOfCDObjects != True:
        IO.display_menu()
    intChoice = IO.user_choice()
    
    # show user current inventory
    if intChoice == 1 and lstOfCDObjects != True:
        IO.display_inventory(lstOfCDObjects)

    # let user add data to the inventory
    elif intChoice == 2:
        if lstOfCDObjects == True:
            lstOfCDObjects = []
        cdID, cdTitle, cdArtist = IO.cd_input()
        newCD = CD(cdID, cdTitle, cdArtist)
        cdID = newCD.compare_ID(lstOfCDObjects)
        newCD = CD(cdID,cdTitle, cdArtist)
        lstOfCDObjects = newCD.cd_added(lstOfCDObjects)
        print('\nThe following data was added to your CD Inventory!\n\n\t', newCD,
              '\n\nChanges will not be kept if data is not Saved.')

    # let user save inventory to file
    elif intChoice == 3 and lstOfCDObjects != True:
        FileIO.write_file(strFileName, lstOfCDObjects)
        print('\nYour Data was Sucessfully Saved!')

    # let user load inventory from file
    elif intChoice == 4 and lstOfCDObjects != True:
        reload_yn = IO.reload_choice()
        
        # lets user load data without saving
        if reload_yn == 1:
            lstOfCDObjects = FileIO.read_file(strFileName)
            print('\nYour data was sucessfully loaded!')
        
        # lets user save and load data
        elif reload_yn == 2:
            FileIO.write_file(strFileName, lstOfCDObjects)
            print('\nYour Data was Sucessfully Saved!')
            lstOfCDObjects = FileIO.read_file(strFileName)
            print('\nYour data was sucessfully loaded!')
        
        # lets user return to main menu
        else: 
            continue

    #let user exit program
    elif intChoice == 5:
        if lstOfCDObjects == True:
            FileIO.delete_file(strFileName)
        yn = IO.exit_choice()
        if yn == 'y':
            intChoice = 5
        else:
            intChoice = 0
        
exit_message = input('Thank you for using the CD inventory program!')
