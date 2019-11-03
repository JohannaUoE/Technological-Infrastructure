#Import the functions that are needed
from PackageTask1 import look_at_file
from PackageTask2 import readNeigh
#testing will be performed with nosetest 3.6
from nose.tools import assert_equal, raises


''' Tests for Task1 '''
#test for corrupt file
def test_numpy():
    #first line of the file should be like this
    should_be = [['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0']]
    #actual first line of the file is this (call function in PackageTask1)
    actually_is = look_at_file('plenty.data')
    #Are both equal?
    assert_equal(actually_is,should_be)

def test_numpy2():
    # testing, that the amount of columns is correct
    #read the first line of the actual data
    actual_data = look_at_file('plenty.data')
    # test the length of the list items against the 11
    assert_equal(len(actual_data[0]),11)


'''Test for Task2'''

def test_neigh():
    #Testing if all neighboorhoods are in the file
    actual_neighboorhood = readNeigh('natural_neighbourhoods.dat')
    # Calling the function that only reads lines that are letters and stores all of them in a list

    # List if neighboorhoods that should be in the file
    should_be_neigh = ['Brunstane/Gilberstoun', 'Newcraighall', 'Magdalene', 'Newbridge', 'Cammo/Strathalmond', 'Muirhouse', 'Granton/West Pilton', 'Broomhouse', 'Ratho Station/Ingliston/Gogar', 'South Queensferry/Dalmeny', 'Kirkliston', 'Gracemount', 'Gilmerton', 'Portobello', 'Liberton', 'Willowbrae', 'Balerno', 'Ratho', 'Calton Hill', 'Blackford', 'Drylaw', 'Morningside', 'Prestonfield', 'Craigmillar/Niddrie', 'Alnwickhill', 'Braids', 'Fairmilehead/Swanston', 'Cameron Toll', 'North Sighthill', 'Wester Coates', 'East Craigs', 'Clermiston/Drumbrae', 'Fountainbridge', 'Ravelston/Murrayfield', 'Silverknowes', 'Forrester Park', 'Baberton', 'Bellevue/Broughton', 'Canonmills', 'Dean Village/West End', 'Riccarton and Hermiston', 'Fountainbridge/Polwarth', 'Juniper Green', 'Currie', 'Joppa', 'Grange', 'Northfield', 'Holyrood Park', 'Duddingston/The Durhams', 'Blackhall', 'Sciennes', 'Duddingston Village and Golf Course', 'Viewforth', 'Oxgangs/Colinton Mains/Firrhill', 'Greenbank', 'Shandon', 'Gayfield/Broughton St', 'Old Town', 'Tollcross', 'Lauriston/Quartermile', 'Colinton/Bonaly', 'Hillside/Easter Rd', 'Maybury', 'South Gyle/Edinburgh Park', 'Telford', 'Warriston', 'Bonnington', 'Pilrig', 'Leith/Easter Rd', 'Crewe Toll', 'Fettes', 'Inverleith', 'Pilton/Royston', 'Granton/Waterfront', 'Trinity', 'Goldenacre', 'Comely Bank', 'Stockbridge', 'Craigleith', 'Orchard Brae', 'Roseburn', 'Balgreen/Saughtonhall', 'Gorgie', 'Dalry', 'West End', 'Bruntsfield', 'Merchiston and Myreside', 'Marchmont', 'Churchill and Greenhill', 'Cramond', 'Southside', 'Newington', 'Dumbiedykes', 'Mountcastle', 'Broughton Rd/Powderhall', 'Newhaven', 'Sighthill', 'Calders', 'Clovenstone', 'Wester Hailes', 'Stenhouse/Saughton', 'Chesser', 'Hutchison/Slateford', 'Parkhead', 'Redhall/Inglis Green', 'Longstone', 'Bankhead', "Davidson's Mains", 'Piershill/Piersfield', 'Marionville', 'Lochend', 'Restalrig', 'Leith', 'Leith Links', 'Craigentinny', 'Seafield', 'Abbeyhill', 'Meadowbank', 'Kingsknowe', 'Dumbryden', 'Craiglockhart', 'Boswall/Wardie', 'Haymarket', 'New Town', 'Greendykes', 'Barnton', 'Corstorphine/North Gyle', 'The Gyle', 'Southhouse', 'Western Harbour', 'Carrick Knowe', 'Comiston', 'Buckstone', 'Turnhouse', 'Bingham', 'Peffermill', 'Niddrie House', 'The Inch', 'Little France/The Royal Infirmary of Edinburgh', 'Fernieside/Ferniehill', 'Moredun', 'The Murrays', 'The Jewel/Cleekims', 'Canongate', 'Wardie Bay', 'Polwarth', 'St Leonards', 'Mortonhall', 'Burdiehouse', 'Corstorphine/Craigmount', 'Corstorphine', 'Corstorphine/Clerwood', 'The Christians/Portobello', 'Ferryfield/Inverleith']

    #testing both list samness
    assert_equal(actual_neighboorhood,should_be_neigh)
