from smartphone import Smartphone
catalog= [
    Smartphone("<Samsung Galaxy>", "<A17>",  "<89266251748>" ),
    Smartphone("<Samsung Galaxy>", "<A27>",  "<89256253515>" ),
    Smartphone("<Samsung Galaxy>", "<A37>",  "<89276261822>" ),
    Smartphone("<Samsung Galaxy>", "<A57>",  "<89246272655>" ),
    Smartphone("<Samsung Galaxy>", "<S26>",  "<89296241906>" )
]

for smartphone in catalog:
    print(smartphone.get_smartphone_info())

