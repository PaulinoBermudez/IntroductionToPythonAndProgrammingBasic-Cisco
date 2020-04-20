country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

print( country )
print( capitals )
print( capitals["South Africa"][1] )

"""
OUTPUT:
=========== RESTART: /home/allan/Dropbox/ETW-BP/list-dicts_sol.py ===========
['Brazil', 'Russia', 'India', 'China', 'South Africa']
{'South Africa': ['Pretoria', 'Cape Town', 'Bloemfontein'], 'India': 'New Delhi', 'Brazil': 'Brasilia', 'Russia': 'Moscow', 'China': 'Beijing'}
Cape Town
>>>
"""
