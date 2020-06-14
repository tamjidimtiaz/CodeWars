''' Just another day in the world of Minecraft, Steve is getting ready to start his next exciting project -- 
building a railway system!

But first, Steve needs to melt some iron ores in the furnace to get the main building blocks of rails -- iron ingots. Alt text

Each iron ingot takes 11 seconds* to produce. Steve needs a lot of them, and he has the following fuel options 
to add into the furnace:

    Buckets of lava, each lasts 800 seconds* Alt text
    Blaze rod, each lasts 120 seconds Alt text
    Coals, each lasts 80 seconds Alt text
    Blocks of Wood, each lasts 15 seconds Alt text
    Sticks, each lasts 1 second* Alt text

In Python: Write a function calc_fuel that calculates the minimum amount of fuel needed 
to produce a certain number of iron ingots. This function should return a dictionary of the form 
{"lava": 2, "blaze rod": 1, "coal": 1, "wood": 0, "stick": 0}
'''
def calc_fuel(n):
    total_time = n*11
    dict = {"lava": 0,
            "blaze rod": 0,
            "coal": 0,
            "wood": 0,
            "stick": 0}
            
    if total_time>800:
        dict["lava"] = total_time//800
        total_time = total_time % 800
    else:
        dict["lava"] = 0
    
    if total_time>120:
        dict["blaze rod"] = total_time//120
        total_time = total_time % 120
    else:
        dict["blaze rod"] = 0
    
    if total_time>80:
        dict["coal"] = total_time//80
        total_time = total_time % 80
    else:
        dict["coal"] = 0
    
    if total_time>15:
        dict["wood"] = total_time//15
        total_time = total_time % 15
    else:
        dict["wood"] = 0   
        
    if total_time>=1:
        dict["stick"] = total_time//1
    else:
        dict["stick"] = 0
    
    return dict  
    # Start coding! You can do it!
