#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
cache = json.loads('''{
  "December 2": [
    "National Fritters Day"
  ], 
  "July 18": [
    "National Caviar Day"
  ], 
  "July 19": [
    "National Daiquiri Day"
  ], 
  "August 30": [
    "National Toasted Marshmallow Day"
  ], 
  "July 12": [
    "National Pecan Pie Day"
  ], 
  "July 13": [
    "National French Fries Day", 
    "National BBQ Day"
  ], 
  "March 23": [
    "National Chips and Dip Day"
  ], 
  "July 11": [
    "National Blueberry Muffin Day"
  ], 
  "July 16": [
    "Fresh Spinach Day", 
    "National Corn Fritter Day"
  ], 
  "July 17": [
    "National Peach Ice Cream Day"
  ], 
  "March 27": [
    "International Whiskey Day"
  ], 
  "July 15": [
    "National Tapioca Pudding Day", 
    "Gummi Worm Day"
  ], 
  "November 8": [
    "National Harvey Wallbanger Day", 
    "Cook Something Bold and Pungent Day", 
    "National Cappuccino Day", 
    "National Shot Day"
  ], 
  "November 9": [
    "National Scrapple Day"
  ], 
  "September 30": [
    "National Hot Mulled Cider Day"
  ], 
  "November 28": [
    "National French Toast Day"
  ], 
  "December 31": [
    "National Champagne Day"
  ], 
  "December 30": [
    "National Bicarbonate of Soda Day"
  ], 
  "November 1": [
    "National Vinegar Day", 
    "National French Fried Clam Day", 
    "National Cook For Your Pets Day"
  ], 
  "November 2": [
    "National Deviled Egg Day"
  ], 
  "November 3": [
    "National Sandwich Day"
  ], 
  "November 4": [
    "National Candy Day"
  ], 
  "September 20": [
    "National Pepperoni Pizza Day", 
    "National Punch Day", 
    "National Rum Punch Day"
  ], 
  "November 7": [
    "National Bittersweet Chocolate with Almonds Day"
  ], 
  "April 2": [
    "National Peanut Butter and Jelly Day"
  ], 
  "April 7": [
    "National Beer Day"
  ], 
  "April 5": [
    "National Caramel Day"
  ], 
  "December 22": [
    "National Date Nut Bread Day"
  ], 
  "November 25": [
    "National Parfait Day"
  ], 
  "November 23": [
    "National Cashew Day", 
    "National Eat A Cranberry Day", 
    "National Espresso Day"
  ], 
  "December 20": [
    "National Sangria Day"
  ], 
  "June 6": [
    "National Applesauce Cake Day"
  ], 
  "June 7": [
    "Chocolate Ice Cream Day"
  ], 
  "June 4": [
    "National Cheese Day", 
    "National Cognac Day"
  ], 
  "June 5": [
    "National Gingerbread Day", 
    "National Moonshine Day"
  ], 
  "June 2": [
    "National Rotisserie Chicken Day", 
    "National Rocky Road Day"
  ], 
  "June 3": [
    "National Chocolate Macaroon Day", 
    "National Egg Day"
  ], 
  "November 29": [
    "Throw Out Your Leftovers Day", 
    "National Lemon Cream Pie Day", 
    "National Chocolates Day"
  ], 
  "November 20": [
    "National Peanut Butter Fudge Day"
  ], 
  "September 29": [
    "National Coffee Day", 
    "National Biscotti Day"
  ], 
  "September 28": [
    "Family Day - A Day to Eat Dinner with Your Children", 
    "National Strawberry Cream Pie Day", 
    "National Drink Beer Day"
  ], 
  "September 25": [
    "National Lobster Day"
  ], 
  "September 27": [
    "National Chocolate Milk Day", 
    "National Corned Beef Hash Day"
  ], 
  "September 26": [
    "National Better Breakfast Day", 
    "National Pancake Day", 
    "National Dumpling Day", 
    "Johnny Appleseed Day"
  ], 
  "September 21": [
    "National Pecan Cookie Day"
  ], 
  "August 1": [
    "National Milkshake Day"
  ], 
  "December 24": [
    "National Eggnog Day"
  ], 
  "November 26": [
    "National Cake Day"
  ], 
  "August 16": [
    "National Rum Day", 
    "World Bratwurst Day"
  ], 
  "December 4": [
    "National Cookie Day"
  ], 
  "July 14": [
    "National Grand Marnier Day", 
    "National Mac & Cheese Day"
  ], 
  "September 11": [
    "National Hot Cross Bun Day"
  ], 
  "August 3": [
    "National Watermelon Day", 
    "National White Wine Day"
  ], 
  "January 5": [
    "National Whipped Cream Day"
  ], 
  "January 3": [
    "National Chocolate Covered Cherry Day"
  ], 
  "January 2": [
    "National Creampuff Day"
  ], 
  "January 1": [
    "National Bloody Mary Day"
  ], 
  "January 9": [
    "National Cassoulet Day"
  ], 
  "March 8": [
    "National Potato Salad Day", 
    "National Peanut Cluster Day"
  ], 
  "March 9": [
    "National Crabmeat Day", 
    "National Meatball Day"
  ], 
  "October 28": [
    "National Chocolate day"
  ], 
  "March 7": [
    "National Crown Roast of Pork Day"
  ], 
  "January 24": [
    "National Peanut Butter Day"
  ], 
  "March 5": [
    "National Cheez Doodle Day"
  ], 
  "January 22": [
    "National Hot Sauce Day"
  ], 
  "March 3": [
    "National Canadian Bacon Day"
  ], 
  "March 1": [
    "National Peanut Butter Lover's Day"
  ], 
  "December 21": [
    "National Hamburger Day"
  ], 
  "Fourth Thursday of November": [
    "Thanksgiving Day"
  ], 
  "February 16": [
    "National Almond Day"
  ], 
  "December 11": [
    "National Noodle Ring Day", 
    "National Have a Bagel Day"
  ], 
  "February 15": [
    "National I Want Butterscotch Day"
  ], 
  "August 22": [
    "National Pecan Torte Day", 
    "National Eat A Peach Day"
  ], 
  "November 6": [
    "National Nachos Day"
  ], 
  "December 13": [
    "National Hot Cocoa Day"
  ], 
  "December 10": [
    "National Lager Day"
  ], 
  "November 18": [
    "National Vichyssoise Day", 
    "National Apple Cider Day"
  ], 
  "August 23": [
    "National Sponge Cake Day"
  ], 
  "November 12": [
    "National Pizza with the Works Except Anchovies Day", 
    "Chicken Soup for the Soul Day", 
    "National Happy Hour Day"
  ], 
  "November 13": [
    "National Indian Pudding Day"
  ], 
  "November 10": [
    "National Vanilla Cupcake Day"
  ], 
  "November 11": [
    "National Sundae Day"
  ], 
  "November 16": [
    "National Fast Food Day"
  ], 
  "November 17": [
    "National Baklava Day", 
    "Homemade Bread Day"
  ], 
  "November 14": [
    "National Pickle Day", 
    "National Spicy Guacamole Day"
  ], 
  "November 15": [
    "National Bundt Day", 
    "National Spicy Hermit Cookie Day", 
    "National Clean Out Your Refrigerator Day"
  ], 
  "First Saturday of February": [
    "Ice Cream for Breakfast Day"
  ], 
  "First Wednesday of November": [
    "National Eating Healthy Day"
  ], 
  "November 19": [
    "Carbonated Beverage with Caffeine Day"
  ], 
  "January 27": [
    "National Chocolate Cake Day"
  ], 
  "June 15": [
    "National Lobster Day"
  ], 
  "June 16": [
    "National Fudge Day"
  ], 
  "June 17": [
    "National Eat Your Vegetables Day"
  ], 
  "June 10": [
    "National Iced Tea Day"
  ], 
  "June 11": [
    "National Corn on the cob day", 
    "National German chocolate cake day"
  ], 
  "June 12": [
    "National Peanut Butter Cookie Day"
  ], 
  "Fourth Thursday of July": [
    "National Chili Dog Day"
  ], 
  "March 2": [
    "National Banana Creme Pie Day"
  ], 
  "Last Thursday of June": [
    "National Bomb Pop Day"
  ], 
  "January 23": [
    "National Pie Day"
  ], 
  "Third Sunday of July": [
    "National Ice Cream Day"
  ], 
  "December 16": [
    "National Chocolate-Covered Anything Day"
  ], 
  "September 1": [
    "National Cherry Popover Day"
  ], 
  "August 31": [
    "Trail Mix Day"
  ], 
  "August 17": [
    "National Vanilla Custard Day"
  ], 
  "July 31": [
    "National Raspberry Cake Day"
  ], 
  "December 17": [
    "National Maple Syrup Day"
  ], 
  "Day after Thanksgiving of November": [
    "Sinkie Day"
  ], 
  "June 28": [
    "National Ceviche Day", 
    "National Tapioca Day"
  ], 
  "July 10": [
    "National Pi\u00f1a colada Day"
  ], 
  "December 15": [
    "National Cupcake Day"
  ], 
  "June 21": [
    "National Peaches 'N' Cream Day"
  ], 
  "June 20": [
    "National Vanilla Milkshake Day", 
    "National Ice Cream Soda Day", 
    "National Kouign Amann Day"
  ], 
  "June 25": [
    "National Catfish Day"
  ], 
  "June 27": [
    "National Orange Blossom Day"
  ], 
  "June 26": [
    "National Chocolate Pudding Day"
  ], 
  "October 14": [
    "National Dessert Day"
  ], 
  "Movable of March": [
    "National Corndog Day"
  ], 
  "October 11": [
    "National Sausage Pizza Day"
  ], 
  "October 18": [
    "National Chocolate Cupcake Day"
  ], 
  "September 2": [
    "National Blueberry Popsicle Day"
  ], 
  "September 3": [
    "National Welsh Rarebit Day"
  ], 
  "December 1": [
    "Eat a Red Apple Day"
  ], 
  "August 25": [
    "National Banana Split Day", 
    "National Whiskey Sour Day"
  ], 
  "September 6": [
    "National Coffee Ice Cream Day"
  ], 
  "September 7": [
    "National Beer Lover's Day", 
    "National Acorn Squash Day", 
    "National Salami Day"
  ], 
  "September 4": [
    "National Macademia Nut Day"
  ], 
  "September 5": [
    "National Cheese Pizza Day"
  ], 
  "December 9": [
    "National Pastry Day"
  ], 
  "September 9": [
    "Wienerschnitzel Day", 
    "National Steak Au Poivre Day"
  ], 
  "January 19": [
    "National Popcorn Day"
  ], 
  "July 23": [
    "National Peanut Butter and Chocolate Day", 
    "National Vanilla Ice Cream Day", 
    "National Hot Dog Day"
  ], 
  "July 22": [
    "National Penuche Fudge Day"
  ], 
  "February 2": [
    "National Tater Tot Day"
  ], 
  "July 20": [
    "National Fortune Cookie Day", 
    "National Lollipop Day"
  ], 
  "July 27": [
    "National Creme Brulee Day", 
    "National Scotch Day"
  ], 
  "July 26": [
    "National Coffee Milkshake Day"
  ], 
  "July 25": [
    "National Hot Fudge Sundae Day"
  ], 
  "February 7": [
    "National Patty Melt Day"
  ], 
  "February 9": [
    "National Pizza Day (at least two slices)", 
    "National Bagel Day"
  ], 
  "July 29": [
    "National Lasagna Day", 
    "National Chicken Wing Day"
  ], 
  "July 28": [
    "Hamburger Day", 
    "National Milk Chocolate Day"
  ], 
  "March 10": [
    "National Blueberry Popover Day"
  ], 
  "March 11": [
    "Oatmeal Nut Waffles Day", 
    "Johnny Appleseed Day"
  ], 
  "March 12": [
    "National Baked Scallops Day"
  ], 
  "October 20": [
    "National Brandied Fruit Day", 
    "National Office Chocolate Day"
  ], 
  "October 23": [
    "National Boston Creme Pie Day"
  ], 
  "October 24": [
    "National Bologna Day", 
    "National Food Day"
  ], 
  "October 25": [
    "National Greasy Food Day"
  ], 
  "September 14": [
    "National Eat a Hoagie Day", 
    "National Cream Filled Donut Day"
  ], 
  "December 8": [
    "National Brownie Day"
  ], 
  "July 21": [
    "National Junk Food Day"
  ], 
  "September 16": [
    "National Guacamole Day", 
    "National Cinnamon-Raisin Bread Day"
  ], 
  "July 8": [
    "National Chocolate with Almonds Day"
  ], 
  "July 9": [
    "National Sugar Cookie Day"
  ], 
  "First Friday of June": [
    "National Donut/Doughnut Day"
  ], 
  "September 17": [
    "National Apple Dumpling Day", 
    "National Monte Cristo sandwich Day"
  ], 
  "July 1": [
    "National Creative Ice Cream Flavor Day", 
    "National Gingersnap Day"
  ], 
  "July 2": [
    "National Anisette Day"
  ], 
  "July 3": [
    "Eat Beans Day", 
    "National Chocolate Wafer Day"
  ], 
  "July 4": [
    "National Caesar Salad Day", 
    "National Spareribs Day", 
    "National Barbecue Day"
  ], 
  "July 5": [
    "National Apple Turnover Day"
  ], 
  "July 6": [
    "Take Your Compliance Coworker to Lunch Day", 
    "National Fried Chicken Day"
  ], 
  "July 7": [
    "Macaroni Day", 
    "National Strawberry Sundae Day"
  ], 
  "July 30": [
    "National Cheesecake Day"
  ], 
  "May 24": [
    "National Escargot Day", 
    "National Schlumpia Day"
  ], 
  "August 15": [
    "National Lemon Meringue Pie Day"
  ], 
  "August 14": [
    "National Creamsicle Day"
  ], 
  "August 13": [
    "National Filet Mignon Day"
  ], 
  "September 12": [
    "National Chocolate Milkshake Day"
  ], 
  "May 23": [
    "National Taffy Day"
  ], 
  "August 10": [
    "National S'more Day"
  ], 
  "August 29": [
    "More Herbs, Less Salt Day", 
    "National Lemon Juice Day", 
    "National Chop Suey Day"
  ], 
  "May 28": [
    "National Brisket Day", 
    "National Burger Day"
  ], 
  "August 19": [
    "National Potato Day"
  ], 
  "August 18": [
    "National Pinot Noir Day"
  ], 
  "April 17": [
    "National Cheeseball Day"
  ], 
  "September 15": [
    "National Cr\u00e8me de Menthe Day", 
    "National Double Cheeseburger Day", 
    "National Linguine Day", 
    "National Cheese Toast Day", 
    "National Butterscotch Cinnamon Pie Day"
  ], 
  "April 15": [
    "National Banana Day"
  ], 
  "August 21": [
    "National Spumoni Day"
  ], 
  "September 10": [
    "National TV Dinner Day"
  ], 
  "April 12": [
    "National Grilled Cheese Sandwich Day"
  ], 
  "April 11": [
    "National Cheese Fondue Day"
  ], 
  "September 13": [
    "National Peanut Day", 
    "International Chocolate Day"
  ], 
  "August 26": [
    "National Cherry Popsicle Day"
  ], 
  "September 18": [
    "National Cheeseburger Day"
  ], 
  "September 19": [
    "National Butterscotch Pudding Day"
  ], 
  "April 19": [
    "National Garlic Day", 
    "National Rice Ball Day"
  ], 
  "August 27": [
    "National Pots De Creme Day", 
    "National Banana Lovers Day"
  ], 
  "August 24": [
    "National Peach Pie Day", 
    "National Waffle Day"
  ], 
  "July 24": [
    "National Tequila Day", 
    "National Drive-Thru Day"
  ], 
  "November 30": [
    "National Mousse Day"
  ], 
  "November 21": [
    "National Stuffing Day"
  ], 
  "October 31": [
    "National Candy Apple Day", 
    "National Caramel Apple Day"
  ], 
  "First Saturday of August": [
    "National Mustard Day"
  ], 
  "October 30": [
    "Haunted Refrigerator Night", 
    "National Candy Corn Day"
  ], 
  "August 28": [
    "National Cherry Turnover Day", 
    "Crackers Over The Keyboard Day"
  ], 
  "May 11": [
    "National Eat What You Want Day"
  ], 
  "April 29": [
    "National Shrimp Scampi Day"
  ], 
  "May 17": [
    "National Walnut Day"
  ], 
  "April 22": [
    "National Jellybean Day"
  ], 
  "April 26": [
    "National Pretzel Day"
  ], 
  "April 27": [
    "National Prime Rib Day"
  ], 
  "April 24": [
    "National Pigs in a Blanket Day"
  ], 
  "April 25": [
    "National Zucchini Bread Day"
  ], 
  "May 4": [
    "National Candied Orange Peel Day"
  ], 
  "May 5": [
    "National Hoagie Day"
  ], 
  "March 31": [
    "National Clams on the Half Shell Day"
  ], 
  "December 25": [
    "National Pumpkin Pie Day"
  ], 
  "February 23": [
    "National Banana Bread Day"
  ], 
  "February 22": [
    "National Margarita Day"
  ], 
  "October 6": [
    "National Noodle Day"
  ], 
  "October 29": [
    "National Oatmeal Day"
  ], 
  "February 29": [
    "National Frog Legs Day (celebration for Leap Day)"
  ], 
  "First Monday of February": [
    "National Frozen Yogurt Day"
  ], 
  "December 27": [
    "National Fruitcake Day"
  ], 
  "October 4": [
    "National Vodka Day", 
    "National Taco Day"
  ], 
  "Third Friday of May": [
    "National Pizza Party Day"
  ], 
  "First Thursday of November": [
    "National Men Make Dinner Day"
  ]
}''')
img_cache = json.loads('''{
  "September 4,National Macademia Nut Day": "http://www.birdsnestfoundation.org/images/stories/macadamia-nuts.jpg", 
  "June 12,National Peanut Butter Cookie Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-peanut-butter-cookie-day-june-12.png?w=490", 
  "March 1,National Peanut Butter Lover's Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-peanut-butter-lovers-day-march-1.png", 
  "September 7,National Salami Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/05/National-Salami-Day-September-7-1-1024x512.jpg", 
  "July 16,National Corn Fritter Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-corn-fritters-day-july-161.png", 
  "August 3,National Watermelon Day": "https://s-media-cache-ak0.pinimg.com/originals/bb/22/6c/bb226cb2974c12734bb0a650406390c4.png", 
  "February 7,National Patty Melt Day": "http://bakedchicago.com/wp-content/uploads/2014/05/ranch-patty-melt_6.jpg", 
  "July 9,National Sugar Cookie Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-sugar-cookie-day-july-9.png?w=660", 
  "November 21,National Stuffing Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Stuffing-Day-November-21-1-1-1024x512.jpg", 
  "November 17,National Baklava Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Baklava-Day-November-17-1-1024x512.jpg", 
  "First Saturday of August,National Mustard Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-mustard-day-first-saturday-in-august.png?w=300", 
  "November 16,National Fast Food Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2013/11/National-Fast-Food-Day-November-16-1-1024x512.jpg", 
  "October 24,National Bologna Day": "http://i.huffpost.com/gen/1423133/images/o-BOLOGNA-DAY-facebook.jpg", 
  "June 28,National Tapioca Day": "https://nationaldaycalendar.files.wordpress.com/2014/07/national-tapioca-pudding-day-july-15.png", 
  "July 23,National Peanut Butter and Chocolate Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/07/national-peanut-butter-day-january-24.png", 
  "November 23,National Espresso Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/11/National-Espresso-Day-November-23-1-1024x512.jpg", 
  "July 23,National Hot Dog Day": "https://cbschicago.files.wordpress.com/2013/07/540285_10152108445344569_1101704757_n.jpg", 
  "First Saturday of February,Ice Cream for Breakfast Day": "http://kardsunlimited.com/wp-content/uploads/2014/01/ice-cream-waffle_5.jpg", 
  "July 7,Macaroni Day": "https://nationaldaycalendar.files.wordpress.com/2014/07/national-macaroni-day-july-7.png?w=980&h=506", 
  "August 28,Crackers Over The Keyboard Day": "https://www.kuriose-feiertage.de/wp-content/uploads/2016/08/Kuriose-Feiertage-28.-August-Kr%C3%BCmel-%C3%BCber-der-Tastatur-Tag-%E2%80%93-der-amerikanische-Crackers-Over-Your-Keyboard-Day-c-2016-Sven-Giese-1.jpg", 
  "Fourth Thursday of November,Thanksgiving Day": "http://images.techtimes.com/data/images/full/281268/journalists-celebrate-thanksgiving.jpg", 
  "September 18,National Cheeseburger Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Cheeseburger-Day-September-18-1-1024x512.jpg", 
  "November 11,National Sundae Day": "http://www.dsl-nw.com/wp-content/uploads/2016/10/sundae.png", 
  "April 5,National Caramel Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/national-caramel-day-april-5-1024x512.png", 
  "December 20,National Sangria Day": "https://s-media-cache-ak0.pinimg.com/originals/d1/d9/19/d1d919a5003b5ec7c667fa82c9eac585.jpg", 
  "July 31,National Raspberry Cake Day": "https://nationaldaycalendar.files.wordpress.com/2014/04/national-raspberry-cake-day-july-31.png", 
  "August 27,National Pots De Creme Day": "http://www.cooksinfo.com/edible.nsf/images/pots-de-creme-day/$file/pots-de-creme-day-tn.jpg", 
  "August 1,National Milkshake Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/05/National-Chocolate-Milkshake-Day-September-12-1-1024x512.jpg", 
  "September 14,National Cream Filled Donut Day": "https://foodimentaryguy.files.wordpress.com/2012/09/www-sodahead-com.jpeg?w=645", 
  "November 26,National Cake Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Cake-Day-November-26-1-1024x512.jpg", 
  "July 26,National Coffee Milkshake Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2016/01/National-Coffee-Milkshake-Day-July-26-1024x512.jpg", 
  "September 15,National Cr\u00e8me de Menthe Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Creme-de-Menthe-Day-September-15-3-1024x512.jpg", 
  "December 2,National Fritters Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Fritters-Day-December-2-1-1024x512.jpg", 
  "August 29,National Lemon Juice Day": "http://thecelebritycafe.com/wp-content/uploads/2016/08/National-Lemon-Juice-Day-1200x545_c.jpg", 
  "January 27,National Chocolate Cake Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-chocolate-cake-day-january-27.png", 
  "August 22,National Eat A Peach Day": "https://s.aolcdn.com/dims-shared/dims3/GLOB/legacy_thumbnail/1060x600/format/jpg/quality/85/http%3A%2F%2Fo.aolcdn.com%2Fhss%2Fstorage%2Fmidas%2F66dbcdd9f4ec8f3eb677ce97b987df4d%2F202222100%2FphpJQnUwn", 
  "July 4,National Barbecue Day": "http://nationaldays.net/wp-content/uploads/2013/05/Bulgarian_barbecue_E1.jpg", 
  "August 14,National Creamsicle Day": "https://s-media-cache-ak0.pinimg.com/originals/a2/12/07/a21207cc662eff6d477c028a3e0cbafa.png", 
  "September 3,National Welsh Rarebit Day": "https://www.dishourtown.com/wp-content/uploads/2016/08/IMG_5153.jpg", 
  "October 29,National Oatmeal Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/national-oatmeal-day-october-29.png?w=300", 
  "April 29,National Shrimp Scampi Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Shrimp-Scampi-Day-April-29-1024x512.jpg", 
  "September 13,National Peanut Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/05/National-Peanut-Day-September-13-1-1024x512.jpg", 
  "January 22,National Hot Sauce Day": "http://www.lamag.com/wp-content/uploads/sites/9/2015/07/hotsauce.jpg", 
  "September 19,National Butterscotch Pudding Day": "https://nationaldaycalendar.com/wp-content/uploads/2015/06/National-Butterscotch-Pudding-Day-September-19-1024x512.jpg", 
  "November 19,Carbonated Beverage with Caffeine Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Carbonated-Beverage-With-Caffeine-Day-November-19-2-1024x512.jpg", 
  "July 27,National Scotch Day": "http://jackiesramblings.com/wp-content/uploads/2016/07/national-scotch-day-july-27.png", 
  "January 9,National Cassoulet Day": "http://cdn-image.foodandwine.com/sites/default/files/styles/rd_fwrd_blog_main_image/public/200510-r-xl-toulouse-style-cassoulet.jpg?itok=VwxCIdlc", 
  "August 26,National Cherry Popsicle Day": "http://3blmedia.com/media/images/Cherry-Popsicle-Day-St.-Jude2-1024x731.jpg", 
  "August 22,National Pecan Torte Day": "https://choosingsimplicity.files.wordpress.com/2009/11/pecantorte.jpg", 
  "December 31,National Champagne Day": "http://1.bp.blogspot.com/-XFq6Al9tTJY/VnhewWnxPkI/AAAAAAAAWYc/Pn2SSprW2Qw/s1600/Screen%2BShot%2B2015-12-21%2Bat%2B2.18.42%2BPM.png", 
  "August 23,National Sponge Cake Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/05/national-sponge-cake-day-august-23.png", 
  "June 4,National Cognac Day": "http://www.velvetbartend.com/bar/wp-content/uploads/2016/06/national-cognac-day-june-4.png", 
  "December 8,National Brownie Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/12/national-brownie-day-december-81.png", 
  "December 21,National Hamburger Day": "http://i4.mirror.co.uk/incoming/article8442443.ece/ALTERNATES/s615/cheesburger.jpg", 
  "September 26,National Better Breakfast Day": "http://goodbelly.com/wp-content/uploads/2015/09/Breakfast-Resizeed-600x400.jpg", 
  "November 9,National Scrapple Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/National-Scrapple-Day-November-9.jpg", 
  "July 15,Gummi Worm Day": "https://mommybase.com/wp-content/uploads/2013/07/gummi-worm-day-july-15.jpg", 
  "September 28,National Drink Beer Day": "https://www.nationaldaycalendar.com/wp-content/uploads/2015/09/NATIONAL-DRINK-BEER-DAY-1.jpg", 
  "June 6,National Applesauce Cake Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-applesauce-cake-day-june-6.png?w=490", 
  "December 1,Eat a Red Apple Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-eat-a-red-apple-day-december-1.png", 
  "July 16,Fresh Spinach Day": "http://www.hellawella.com/sites/hellawella.com/files/styles/default/public/images/spinach.jpg?itok=d8YGZXo6", 
  "June 2,National Rocky Road Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-rocky-road-day-june-2.png", 
  "Day after Thanksgiving of November,Sinkie Day": "https://www.kuriose-feiertage.de/wp-content/uploads/2015/11/Kuriose-Feiertage-27.-November-2015-%C3%9Cber-der-Sp%C3%BCle-Essen-Tag-in-den-USA-%E2%80%93-der-amerikanische-Sinkie-Day-c-2015-Sven-Giese-1.jpg", 
  "July 6,Take Your Compliance Coworker to Lunch Day": "https://s-media-cache-ak0.pinimg.com/736x/ac/00/72/ac007256d24ea58b5119753b5fa7ef83.jpg", 
  "January 2,National Creampuff Day": "https://static1.squarespace.com/static/553b26fde4b08ceb08a4242c/t/5686a81740667a38690c422d/1451665432938/", 
  "August 27,National Banana Lovers Day": "https://static.wixstatic.com/media/d3aeaa2d4f9d498da18e60d469a2cf0b.jpg/v1/fill/w_626,h_417/d3aeaa2d4f9d498da18e60d469a2cf0b.jpg", 
  "August 30,National Toasted Marshmallow Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/05/national-toasted-marshmallow-day-august-30.png?w=660", 
  "September 15,National Cheese Toast Day": "http://nationaldaycalendar.com/wp-content/uploads/2015/07/national-cheese-toast-day-september-15.png?w=660", 
  "November 30,National Mousse Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Mousse-Day-November-30-1-1024x512.jpg", 
  "February 15,National I Want Butterscotch Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-butterscotch-brownie-day-may-9.png", 
  "July 13,National French Fries Day": "http://www.hot933hits.com/wp-content/uploads/sites/265/2016/07/national-french-fry-day-july-13.png", 
  "First Friday of June,National Donut/Doughnut Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-doughnut-day-first-friday-in-june.png?w=490", 
  "October 30,National Candy Corn Day": "http://media.graytvinc.com/images/810*606/candy-corn2.jpg", 
  "August 25,National Banana Split Day": "https://s-media-cache-ak0.pinimg.com/originals/9c/bb/a4/9cbba46fbab79f65c6bbf3a494e3ab37.png", 
  "November 2,National Deviled Egg Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/11/default/national_deviled_egg_day_0_1478060602.jpg", 
  "October 28,National Chocolate day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/national-chocolate-day-2.png?w=300", 
  "April 26,National Pretzel Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Pretzel-Day-April-26-1024x512.jpg", 
  "December 16,National Chocolate-Covered Anything Day": "http://menuofmusings.com/wp-content/uploads/2013/12/National-Chocolate-Covered-Anything-Day-2-716x1024.jpg", 
  "October 4,National Taco Day": "https://t.rmncdn.com/blog/2016/09/NationalTacoDay2016-1474926323.jpg", 
  "November 23,National Cashew Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Cashew-Day-November-23-1-1024x512.jpg", 
  "September 25,National Lobster Day": "http://i2.cdn.turner.com/cnn/2011/images/06/14/lobster_t1larg.jpg", 
  "September 26,National Dumpling Day": "http://nationaldaycalendar.com/wp-content/uploads/2015/05/national-dumpling-day-september-26.png", 
  "September 17,National Apple Dumpling Day": "https://365reasonstocelebrate.files.wordpress.com/2013/09/dutch-apple-dumplings.jpg", 
  "May 24,National Schlumpia Day": "https://schlumpia.files.wordpress.com/2016/09/roshschlumpia2.jpg?w=1200", 
  "October 4,National Vodka Day": "https://drinks-dvq6ncf.netdna-ssl.com/wordpress/wp-content/uploads/2016/08/Shot-of-vodka.jpg", 
  "First Monday of February,National Frozen Yogurt Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2015/02/National-Frozen-Yogurt-Day-1024x512.jpg", 
  "Movable of March,National Corndog Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2016/03/National-Corndog-Day-Changes-Annually-1024x512.jpg", 
  "August 16,National Rum Day": "https://img.memesuper.com/dfab3699e7e969571108b4390629f597_its-also-national-rum-day-national-rum-day-memes_1024-512.png", 
  "December 17,National Maple Syrup Day": "https://kiddieacademy.com/wp-content/uploads/2016/10/national-maple-syrup-day.png", 
  "July 24,National Tequila Day": "https://s-media-cache-ak0.pinimg.com/originals/d5/6d/82/d56d825f3645713a784a1f06bd3df0e0.png", 
  "December 25,National Pumpkin Pie Day": "https://s-media-cache-ak0.pinimg.com/originals/0b/90/18/0b901857b988d84b374910fd1b14b005.png", 
  "February 16,National Almond Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-almond-day-february-16.png", 
  "July 2,National Anisette Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-anisette-day-july-2.png", 
  "July 27,National Creme Brulee Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-creme-brulee-day-july-27.png?w=300", 
  "July 14,National Grand Marnier Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-grand-marnier-day-july-14.png", 
  "September 20,National Punch Day": "http://aviationgin.com/wp-content/uploads/pimms_punch.jpg?x36112", 
  "September 15,National Double Cheeseburger Day": "https://foodimentaryguy.files.wordpress.com/2012/09/epicfoodsatl-com.jpg", 
  "August 24,National Peach Pie Day": "https://foodimentaryguy.files.wordpress.com/2014/08/www-pillsbury-com.jpg", 
  "November 8,National Cappuccino Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-cappuccino-day-november-8.png?w=150", 
  "August 13,National Filet Mignon Day": "https://s-media-cache-ak0.pinimg.com/originals/aa/15/1e/aa151e30796a42df52cb1e79f750ebdd.png", 
  "June 27,National Orange Blossom Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-orange-blossom-day-june-27.png", 
  "November 1,National French Fried Clam Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-fried-clams-day-november-1.png", 
  "May 24,National Escargot Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-escargot-day-may-24.png?w=490", 
  "September 27,National Chocolate Milk Day": "http://thehilandhome.com/wp-content/uploads/NATIONAL-CHOCOLATE-MILK-DAY-2.jpg", 
  "June 10,National Iced Tea Day": "https://s-media-cache-ak0.pinimg.com/originals/d8/30/29/d83029afe2f283099dcb279149f917ee.png", 
  "March 8,National Potato Salad Day": "https://pbs.twimg.com/media/C5mqMwIVUAAgkSf.jpg", 
  "February 29,National Frog Legs Day (celebration for Leap Day)": "https://37fbcb1a70bce7494a3e-9a79802e13701ed93814bf9bdf1cf22c.ssl.cf2.rackcdn.com/11038299", 
  "October 23,National Boston Creme Pie Day": "http://1.bp.blogspot.com/-mBrjpPKsLKU/UIabUTP6YaI/AAAAAAAALd4/4EGyj3EJgF0/s1600/Pudding+si+Boston+Cream+Pie+3:29:68.png", 
  "April 24,National Pigs in a Blanket Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Pigs-in-a-Blanket-Day-April-24-1024x512.jpg", 
  "November 8,National Shot Day": "http://images1.houstonpress.com/imager/u/original/6409061/dsc_6729.jpg", 
  "November 1,National Vinegar Day": "https://foodimentaryguy.files.wordpress.com/2016/12/can-use-white-vinegar-instead-cider-vinegar_e7ec20fe7d24a9b7.jpg?w=880", 
  "April 19,National Rice Ball Day": "http://nationaldays.net/wp-content/uploads/2013/04/13075851134_a35e278cbc_b.jpg", 
  "July 20,National Lollipop Day": "http://dessertfirstgirl.com/images/2015/07/LollipopLove-cover-large-e1437429508718.jpg", 
  "September 26,National Pancake Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/National-Pancake-Day-%E2%80%93-IHOP-Changes-Annually-1024x512.jpg", 
  "December 15,National Cupcake Day": "https://foodimentaryguy.files.wordpress.com/2012/06/lemoncupcake.jpg?w=645", 
  "November 1,National Cook For Your Pets Day": "https://www.healthypawspetinsurance.com/blog/wp-content/uploads/cooking-with-dog-640x420.jpg", 
  "March 11,Johnny Appleseed Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Johnny-Appleseed-Day-March-11-1024x512.jpg", 
  "April 2,National Peanut Butter and Jelly Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/National-Peanut-Butter-and-Jelly-Day-April-2-1024x512.jpg", 
  "September 28,Family Day - A Day to Eat Dinner with Your Children": "http://4.bp.blogspot.com/-z-7x8JDU_UE/TlvnNqE8zjI/AAAAAAAAAIM/NIIOJelZmkg/s1600/Family_Eats_together_flier.JPG", 
  "September 30,National Hot Mulled Cider Day": "https://www.travelodge.co.uk/blog/wp-content/uploads/2014/08/iStock_000021949250Small.jpg", 
  "July 10,National Pi\u00f1a colada Day": "https://s-media-cache-ak0.pinimg.com/originals/f2/af/7f/f2af7f57be5d390fc68d517e06eb02ee.png", 
  "October 31,National Candy Apple Day": "https://s-media-cache-ak0.pinimg.com/736x/d2/1f/49/d21f4937bc953cca6f26f8a02ee05953.jpg", 
  "July 6,National Fried Chicken Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-fried-chicken-day-july-6.png", 
  "November 25,National Parfait Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Parfait-Day-November-25-2-1024x512.jpg", 
  "March 7,National Crown Roast of Pork Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Crown-of-Roast-Pork-March-7-1024x512.jpg", 
  "September 20,National Rum Punch Day": "http://www.rumshopryan.com/wp-content/uploads/2015/09/AFROHEAD-Grapefruit-Punch.jpg", 
  "August 16,World Bratwurst Day": "https://www.askchefdennis.com/wp-content/uploads/2016/08/jb-2.jpg", 
  "October 31,National Caramel Apple Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Caramel-Apple-Day-October-31-1-1024x512.jpg", 
  "August 19,National Potato Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-cook-a-sweet-potato-day-february-22.png", 
  "February 9,National Pizza Day (at least two slices)": "https://t.rmncdn.com/blog/2017/02/NationalPizzaDayDeals-1486423863.jpg", 
  "First Thursday of November,National Men Make Dinner Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/11/default/national_men_make_dinner_day_n_0_1478148912.png", 
  "July 25,National Hot Fudge Sundae Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/07/default/national_hot_fudge_sundae_day__0_1469439401.png", 
  "November 20,National Peanut Butter Fudge Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Peanut-Butter-Fudge-Day-November-20-1-1-1024x512.jpg", 
  "November 29,National Chocolates Day": "http://www.deltadentalarblog.com/wp-content/uploads/2014/09/Chocolate.jpeg", 
  "December 30,National Bicarbonate of Soda Day": "https://i1.wp.com/www.nationaldaycalendar.com/wp-content/uploads/2014/06/national-bicarbonate-of-soda-day-december-30-1024x512.png", 
  "September 6,National Coffee Ice Cream Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/05/National-Coffee-Ice-Cream-Day-September-6-1-1024x512.jpg", 
  "August 18,National Pinot Noir Day": "https://pbs.twimg.com/media/CqKqxocWAAAk2vC.jpg", 
  "June 17,National Eat Your Vegetables Day": "http://healthylivinghowto.com/wp-content/uploads/2013/06/eat-your-vegetables.jpg", 
  "July 29,National Chicken Wing Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/07/default/national_chicken_wing_day_july_0_1469793473.png", 
  "June 11,National German chocolate cake day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-German-Chocolate-Cake-Day-June-11-1024x512.jpg", 
  "December 13,National Hot Cocoa Day": "https://vasafitness.com/content/uploads/2014/12/shutterstock_237070627.jpg", 
  "November 29,National Lemon Cream Pie Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/08/default/national_lemon_meringue_pie_da_0_1471244908.jpg", 
  "March 27,International Whiskey Day": "https://i2.wp.com/happydays-365.com/wp-content/uploads/2017/03/Whisky.jpg?resize=600%2C398&ssl=1", 
  "September 26,Johnny Appleseed Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Johnny-Appleseed-Day-March-11-1024x512.jpg", 
  "June 20,National Ice Cream Soda Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-ice-cream-soda-day-june-20.png", 
  "March 10,National Blueberry Popover Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Blueberry-Popover-Day-March-10-1024x512.jpg", 
  "November 18,National Vichyssoise Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Vichyssoise-Day-November-18-1-1-1024x512.jpg", 
  "September 1,National Cherry Popover Day": "http://thefoodiepatootie.com/wp-content/uploads/2014/03/blueberry-lemon-popovers-recipe-682x1024.png", 
  "June 20,National Kouign Amann Day": "https://dostuff-assets.s3.amazonaws.com/property_asset/22653/Screen_Shot_2015-06-18_at_9.51.17_AM.png", 
  "November 12,National Happy Hour Day": "http://thelatinkitchen.com/sites/default/files/styles/slideshows/public/slide/888/national_happy_hour_day_shutterstock_.jpg?itok=8SWcaj_A", 
  "Third Sunday of July,National Ice Cream Day": "https://s-media-cache-ak0.pinimg.com/originals/0d/91/c6/0d91c68c47427d33541414f310a3bebe.png", 
  "May 28,National Burger Day": "http://www.tampabay.com/resources/images/blogs-photo/rendered/2015/05/01WEB_NatBurgerDay052915_750x525_8col.jpg", 
  "March 2,National Banana Creme Pie Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-banana-cream-pie-day-march-2.png", 
  "July 28,National Milk Chocolate Day": "https://s-media-cache-ak0.pinimg.com/originals/44/03/b9/4403b9302ddee6b5a67314f74c4aa5f6.png", 
  "May 17,National Walnut Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-walnut-day-june-17.png?w=490", 
  "June 26,National Chocolate Pudding Day": "https://nationaldaycalendar.files.wordpress.com/2014/04/national-chocolate-pudding-day-june-26.png", 
  "April 7,National Beer Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/03/national-beer-day-april-7.png", 
  "August 21,National Spumoni Day": "http://www.craftycookingmama.com/wp-content/uploads/2014/08/081.jpg", 
  "August 31,Trail Mix Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/05/National-Trail-Mix-Day-August-31-1024x512.jpg", 
  "July 7,National Strawberry Sundae Day": "https://civilwartalk.com/proxy.php?image=http%3A%2F%2Fnationaldaycalendar.com%2Fwp-content%2Fuploads%2F2014%2F04%2Fnational-strawberry-sundae-day-july-7.png%3Fw%3D300&hash=4bc7805e76d2ff22b0e7952e8ba2b19e", 
  "July 3,Eat Beans Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-eat-your-beans-day-july-3.png?w=300", 
  "August 25,National Whiskey Sour Day": "https://www.familiesonline.co.uk/images/default-source/local/kensington-and-chelsea/in-the-know-images/whiskey-sour.jpg?sfvrsn=0", 
  "June 25,National Catfish Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-catfish-day-june-251.png", 
  "September 29,National Biscotti Day": "https://foodimentaryguy.files.wordpress.com/2017/02/d53e3f4c5e564a5b03889e621234f419.jpg?w=736", 
  "January 3,National Chocolate Covered Cherry Day": "https://boardgamegeek.com/camo/c2bd641d279f7c89ab1a4202e6d9b58057cd9526/687474703a2f2f7777772e6e6174696f6e616c64617963616c656e6461722e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f30362f4e6174696f6e616c2d43686f636f6c6174652d436f76657265642d4368657272792d4461792d4a616e756172792d33312d31303234783531322e6a7067", 
  "July 12,National Pecan Pie Day": "https://s-media-cache-ak0.pinimg.com/originals/83/76/08/837608332cd8f0f525ff9770aab06267.png", 
  "September 2,National Blueberry Popsicle Day": "https://media.licdn.com/mpr/mpr/p/6/005/083/1d0/1a95733.jpg", 
  "August 24,National Waffle Day": "https://s-media-cache-ak0.pinimg.com/originals/e0/1f/4c/e01f4c14c48fbf28b28227026c3e6e86.png", 
  "November 12,Chicken Soup for the Soul Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Chicken-Soup-for-the-Soul-Day-November-12-1-1024x512.jpg", 
  "November 8,National Harvey Wallbanger Day": "http://cdna.tid.al/7438c5f3f0e9bbf5dfce32ed1d45fa4d570e0855_600.jpg", 
  "July 1,National Creative Ice Cream Flavor Day": "https://2.bp.blogspot.com/-G_teIBMvXr8/V3Z_-tbKLsI/AAAAAAAABrE/Yfyos4G-ByYiFPbBuTuRzW4Y8ZERTuwcgCLcB/s1600/national-creative-ice-cream-flavors-day-july-1.png", 
  "August 29,National Chop Suey Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/05/national-chop-suey-day-august-29.png?w=660", 
  "June 2,National Rotisserie Chicken Day": "http://www.themamamaven.com/wp-content/uploads/2015/06/BOS-3038-640x640-wholechicken3.jpg", 
  "May 11,National Eat What You Want Day": "http://www.partyexcuses.com/images/uploads/holidayimages/all_you_can_eat_day.jpg", 
  "June 5,National Gingerbread Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Gingerbread-Day-June-5.jpg", 
  "October 20,National Office Chocolate Day": "https://media.glassdoor.com/l/8a/96/06/98/celebrating-national-chocolate-day-at-our-corporate-office.jpg", 
  "April 11,National Cheese Fondue Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/National-Cheese-Fondue-Day-April-11-1024x512.jpg", 
  "February 23,National Banana Bread Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-banana-bread-day-february-23.png", 
  "March 12,National Baked Scallops Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Baked-Scallops-Day-March-12-1024x512.jpg", 
  "July 11,National Blueberry Muffin Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-blueberry-muffin-day-july-11.png?w=490", 
  "September 15,National Butterscotch Cinnamon Pie Day": "http://www.cookiemadness.net/wp-content/uploads/2014/01/butterscotch-cream-pie2.jpg", 
  "July 23,National Vanilla Ice Cream Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-vanilla-ice-cream-day-july-23-1.png", 
  "September 20,National Pepperoni Pizza Day": "http://www.burn-blog.com/wp-content/uploads/2012/02/Heart_Shaped_Pizza.jpg", 
  "July 22,National Penuche Fudge Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/07/national-penuche-fudge-day-july-22.png", 
  "December 22,National Date Nut Bread Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Date-Nut-Bread-Day-December-22-1024x512.jpg", 
  "February 9,National Bagel Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-bagel-day-february-9.png?w=300", 
  "June 20,National Vanilla Milkshake Day": "http://assets.discountqueens.com/uploads/Cheesecake-Milkshake.jpg", 
  "October 6,National Noodle Day": "https://s-media-cache-ak0.pinimg.com/originals/77/f9/f9/77f9f986241cbab0600bd702ab5ece05.jpg", 
  "November 12,National Pizza with the Works Except Anchovies Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Pizza-with-the-Works-Except-Anchovies-Day-November-12-1-1024x512.jpg", 
  "Fourth Thursday of July,National Chili Dog Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/07/national-chili-dog-day-last-thursday-in-july.png?w=300", 
  "September 16,National Guacamole Day": "http://www.foodieoncampus.com/wp-content/uploads/2014/11/guac.jpg", 
  "September 10,National TV Dinner Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/05/National-TV-Dinner-Day-September-10-1024x512.jpg", 
  "September 14,National Eat a Hoagie Day": "http://nationaldaycalendar.com/wp-content/uploads/2015/09/National-Hoagie-Day-1024x512.jpg", 
  "September 16,National Cinnamon-Raisin Bread Day": "http://donnacoulling.com/wp-content/uploads/2015/09/National-Cinnamon-Raisin-Bread-Day-September-16-1024x512.jpg", 
  "July 8,National Chocolate with Almonds Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-chocolate-with-almonds-day-july-8.png?w=490", 
  "December 27,National Fruitcake Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/national-fruitcake-day-december-27.png", 
  "April 27,National Prime Rib Day": "http://cobornsblog.com/wp-content/uploads/2015/04/PrimeRibDayHeader.jpg", 
  "October 11,National Sausage Pizza Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/10/default/national_sausage_pizza_day_oct_0_1476162763.jpg", 
  "January 24,National Peanut Butter Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/07/national-peanut-butter-day-january-24.png", 
  "September 13,International Chocolate Day": "https://www.calendarlabs.com/holidays/images/international-chocolate-day.jpg", 
  "October 30,Haunted Refrigerator Night": "http://img15.deviantart.net/fdc8/i/2014/141/e/d/10_haunted_refrigerator_night_by_rspdan-d7j8glw.jpg", 
  "March 11,Oatmeal Nut Waffles Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Oatmeal-Nut-Waffles-Day-March-11-1024x512.jpg", 
  "April 19,National Garlic Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Garlic-Day-April-19-1024x512.jpg", 
  "September 7,National Beer Lover's Day": "https://s-media-cache-ak0.pinimg.com/736x/0c/dc/0a/0cdc0aa0b62c47a6a8f8e961b0fd2ccd.jpg", 
  "November 3,National Sandwich Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/National-Sandwich-Day-November-3-1-1024x512.jpg", 
  "March 9,National Meatball Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Meatball-Day-March-9-1024x512.jpg", 
  "November 28,National French Toast Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-French-Toast-Day-November-28-1-1-1024x512.jpg", 
  "January 1,National Bloody Mary Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2016/12/National-Bloody-Mary-Day-January-1.jpg", 
  "February 22,National Margarita Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Margarita-Day-February-22.jpg", 
  "July 21,National Junk Food Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-junk-food-day-july-21-1.png", 
  "July 1,National Gingersnap Day": "https://s-media-cache-ak0.pinimg.com/originals/d8/73/ab/d873ab85a557258e6846fbd676cc26f3.png", 
  "October 20,National Brandied Fruit Day": "https://s-media-cache-ak0.pinimg.com/originals/d5/2e/54/d52e54074a5ab8258ed657a4af3730ee.jpg", 
  "June 11,National Corn on the cob day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-corn-on-the-cob-day-june-11.png?w=300", 
  "June 7,Chocolate Ice Cream Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-chocolate-ice-cream-day-june-7.png", 
  "April 15,National Banana Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-banana-bread-day-february-23.png", 
  "First Wednesday of November,National Eating Healthy Day": "https://i.ytimg.com/vi/Iu7MRh5kZRw/hqdefault.jpg", 
  "July 24,National Drive-Thru Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-drive-thru-day-july-24.png?w=300", 
  "November 14,National Spicy Guacamole Day": "http://alarishealth.com/wp-content/uploads/2016/11/national-spicy-quacamole-day.png", 
  "June 15,National Lobster Day": "http://www.lobsterfrommaine.com/wp-content/uploads/2015/08/National-Lobster-Day-3-768x768.jpg", 
  "June 16,National Fudge Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-fudge-day-june-16.png", 
  "July 18,National Caviar Day": "http://1.bp.blogspot.com/-nXDbswnGv74/VaefCPfWCMI/AAAAAAAA7NY/uvtOQcqgLEY/s1600/national-caviar-day-july-18.png", 
  "July 30,National Cheesecake Day": "https://s-media-cache-ak0.pinimg.com/originals/35/88/19/3588192f47b746366f7b92b41172743b.png", 
  "August 28,National Cherry Turnover Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/05/National-Cherry-Turnovers-Day-August-28-1024x512.jpg", 
  "July 17,National Peach Ice Cream Day": "https://nationaldaycalendar.files.wordpress.com/2014/04/national-peach-ice-cream-day-july-17.png", 
  "November 7,National Bittersweet Chocolate with Almonds Day": "http://i2.cdn.turner.com/cnn/dam/assets/111104120726-chocolate-almonds-story-top.jpg", 
  "September 12,National Chocolate Milkshake Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/05/National-Chocolate-Milkshake-Day-September-12-1-1024x512.jpg", 
  "October 24,National Food Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/National-Food-Day-October-24-1-1024x512.jpg", 
  "July 13,National BBQ Day": "https://cookdazzle.files.wordpress.com/2012/05/bbq.jpg", 
  "March 5,National Cheez Doodle Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Cheese-Doodle-Day-March-5-1024x512.jpg", 
  "July 15,National Tapioca Pudding Day": "https://nationaldaycalendar.files.wordpress.com/2014/07/national-tapioca-pudding-day-july-15.png", 
  "June 5,National Moonshine Day": "http://images.askmen.com/fine_living/wine_dine_archive/national-moonshine-day_1433299376.jpg", 
  "April 25,National Zucchini Bread Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Zucchini-Bread-Day-April-25-1024x512.jpg", 
  "November 13,National Indian Pudding Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Indian-Pudding-Day-November-13-1024x512.jpg", 
  "October 18,National Chocolate Cupcake Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/National-Chocolate-Cupcake-Day-October-181-1024x512.jpg", 
  "July 3,National Chocolate Wafer Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/07/national-chocolate-wafer-day-july-3.png", 
  "December 24,National Eggnog Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Eggnog-Day-December-241-1024x512.jpg", 
  "July 20,National Fortune Cookie Day": "http://www.vegasnews.com/wp-content/uploads/Fortune-Cookies-588.jpg", 
  "December 11,National Have a Bagel Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/06/national-bagel-day-february-9.png?w=300", 
  "August 17,National Vanilla Custard Day": "http://www.discountqueens.com/uploads/august-17.png", 
  "July 14,National Mac & Cheese Day": "http://kwwl.images.worldnow.com/images/6169806_G.jpg", 
  "September 27,National Corned Beef Hash Day": "http://blog.brentsdeli.com/wp-content/uploads/2013/09/corned-beef-hash.jpg", 
  "January 23,National Pie Day": "https://cdn.daysoftheyear.com/wp-content/images/pie-day-e1451319806549-808x380.jpg", 
  "Third Friday of May,National Pizza Party Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/national-pizza-party-day-third-friday-in-may.png", 
  "November 29,Throw Out Your Leftovers Day": "http://i.dailymail.co.uk/i/pix/2015/04/08/23/275964C800000578-3031102-image-m-28_1428531562192.jpg", 
  "March 31,National Clams on the Half Shell Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/National-Clams-On-The-Half-Shell-Day-1024x512.jpg", 
  "March 8,National Peanut Cluster Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/National-Peanut-Cluster-Day-March-8-1024x512.jpg", 
  "June 3,National Egg Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2016/06/National-Egg-Day.jpg", 
  "December 9,National Pastry Day": "https://pbs.twimg.com/media/B4aQ84UIcAAy1Ap.jpg", 
  "June 28,National Ceviche Day": "http://image.nola.com/home/nola-media/width960/img/photogallery/photo/5e6c4e9a83851cf09fd0c8feeda9fdd0.JPG", 
  "May 5,National Hoagie Day": "https://foodimentaryguy.files.wordpress.com/2011/05/befunky-design4.jpg", 
  "November 15,National Spicy Hermit Cookie Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Spicy-Hermit-Cookie-Day-November-15-1-1024x512.jpg", 
  "December 4,National Cookie Day": "http://images.pcmac.org/SiSFiles/Schools/FL/GadsdenCounty/GeorgeWMunroeElementary/Uploads/Other/%7B027DA19D-212F-4347-BDE6-B00664ABB797%7D_national-cookie-day-december-4.png", 
  "November 23,National Eat A Cranberry Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Eat-a-Cranberry-Day-November-23-1-1024x512.jpg", 
  "August 10,National S'more Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/08/default/national_smores_day_0_1470821505.jpg", 
  "July 4,National Caesar Salad Day": "http://cdn.patch.com/users/21896555/2014/07/T800x600/4415ec6dbdd03b2cb43eb430c8f67968.jpg", 
  "September 7,National Acorn Squash Day": "http://jackiesramblings.com/wp-content/uploads/2016/09/National-Acorn-Squash-Day-September-7-1024x512.jpg", 
  "November 10,National Vanilla Cupcake Day": "http://hipnewjersey.com/wp-content/uploads/2016/11/Paleo-Vanilla-Cupcakes-672x372.jpg", 
  "June 4,National Cheese Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/national-cheese-day-june-4.png", 
  "April 17,National Cheeseball Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/National-Cheeseball-Day-April-17-1024x512.jpg", 
  "November 8,Cook Something Bold and Pungent Day": "https://pbs.twimg.com/media/CwusYqiVEAAq90g.jpg", 
  "May 28,National Brisket Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-brisket-day-may-28.png?w=490", 
  "November 6,National Nachos Day": "https://s-media-cache-ak0.pinimg.com/originals/55/48/fa/5548fa29053728c63c2c813814c52f03.jpg", 
  "July 29,National Lasagna Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/04/national-lasagna-day-july-29.png?w=300", 
  "October 14,National Dessert Day": "http://americleaninc.com/wp-content/uploads/Dessert.jpg", 
  "September 11,National Hot Cross Bun Day": "http://i1.wp.com/nationaldaycalendar.com/wp-content/uploads/2014/05/National-Hot-Cross-Bun-Day-September-11.jpg", 
  "September 28,National Strawberry Cream Pie Day": "https://s-media-cache-ak0.pinimg.com/originals/e6/f6/fb/e6f6fb44ad2e3ddfbd1bbfd83c3606ff.jpg", 
  "November 15,National Bundt Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Bundt-Day-November-15-1-1024x512.jpg", 
  "November 18,National Apple Cider Day": "https://foodimentaryguy.files.wordpress.com/2014/11/snappymeal-com.jpg", 
  "July 28,Hamburger Day": "http://res.cloudinary.com/sagacity/image/upload/c_crop,h_376,w_620,x_0,y_0/c_scale,w_1080/v1401294120/burgers-cover_xhlyo8_lqjcck.jpg", 
  "March 9,National Crabmeat Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Crabmeat-Day-March-9-1024x512.jpg", 
  "August 29,More Herbs, Less Salt Day": "http://www.dailyholidayblog.com/wp-content/uploads/2013/08/7_spppicesss053.jpg", 
  "August 15,National Lemon Meringue Pie Day": "http://img.ccrd.clearchannel.com/media/mlib/1291/2016/08/default/national_lemon_meringue_pie_da_0_1471244908.jpg", 
  "September 17,National Monte Cristo sandwich Day": "http://flicksandfood.com/wp-content/uploads/2015/09/unnamed7-e1442419622536.jpg", 
  "December 10,National Lager Day": "https://cdn20.patchcdn.com/users/22832903/20161208/042043/styles/T600x450/public/article_images/nationallagerday-1481231996-1026.jpg", 
  "September 29,National Coffee Day": "http://nationaldaycalendar.com/wp-content/uploads/2015/09/National-Coffee-Day-Specials-1024x512.jpg", 
  "December 11,National Noodle Ring Day": "https://nationaldaycalendar.files.wordpress.com/2014/06/national-noodle-ring-day.png", 
  "July 19,National Daiquiri Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-daiquiri-day-july-19.png?w=300", 
  "October 25,National Greasy Food Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/10/national-greasy-foods-day.png", 
  "November 17,Homemade Bread Day": "http://thumbs.ifood.tv/files/image/73/4a/568831-homemade-bread.jpg", 
  "April 22,National Jellybean Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/national-jelly-bean-day-april-22.png", 
  "September 5,National Cheese Pizza Day": "http://nationaldaycalendar.com/wp-content/uploads/2014/05/National-Cheese-Pizza-Day-September-5-1024x512.jpg", 
  "April 12,National Grilled Cheese Sandwich Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/03/National-Grilled-Cheese-Sandwich-Day-April-12-1024x512.jpg", 
  "November 14,National Pickle Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Pickle-Day-November-14-1-1024x512.jpg", 
  "September 9,National Steak Au Poivre Day": "https://s-media-cache-ak0.pinimg.com/736x/a5/ea/87/a5ea87f2a5005d027fe8feb84066b5a0.jpg", 
  "November 15,National Clean Out Your Refrigerator Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Clean-Out-Your-Refrigerator-Day-November-15-1-1024x512.jpg", 
  "March 3,National Canadian Bacon Day": "http://www.seriouseats.com/recipes/assets_c/2012/03/20110320-198179-canadian-bacon-thumb-625xauto-227205.jpg", 
  "February 2,National Tater Tot Day": "https://foodimentaryguy.files.wordpress.com/2017/01/img_3488edit.jpg?w=650", 
  "June 3,National Chocolate Macaroon Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/04/National-Chocolate-Macaroon-Day-June3-1024x512.jpg", 
  "January 19,National Popcorn Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Popcorn-Day-January-19-1024x512.jpg", 
  "March 23,National Chips and Dip Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Chip-and-Dip-Day-March-23-1024x512.jpg", 
  "July 5,National Apple Turnover Day": "http://2.bp.blogspot.com/-zcJ9bn8_aIM/T_XKsa5V4fI/AAAAAAAAA_Q/fDNMmemckr8/s1600/Apple+Turnovers.jpg", 
  "May 23,National Taffy Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/04/national-taffy-day-may-23.png?w=490", 
  "June 21,National Peaches 'N' Cream Day": "http://3.bp.blogspot.com/_CDzmgA25INQ/TB-uYe3MTuI/AAAAAAAAAjs/uitZkS8dy34/s1600/Drunken+Peaches+N+Cream.jpg", 
  "September 21,National Pecan Cookie Day": "http://www.nationaldaycalendar.com/wp-content/uploads/2014/06/National-Pecan-Cookie-Day-September-21-1-1024x512.jpg", 
  "July 4,National Spareribs Day": "http://cdn0.wideopencountry.com/wp-content/uploads/2015/07/bigstock-Slabs-Of-Bbq-Spare-Ribs-5189179.jpg", 
  "August 3,National White Wine Day": "http://www.partyexcuses.com/images/uploads/holidayimages/bigstock-White-Wine-5090589.jpg", 
  "May 4,National Candied Orange Peel Day": "http://4.bp.blogspot.com/-wJOGmfScl5A/VUdmIVV5GBI/AAAAAAAA4zY/k4gQ3oCBgcY/s1600/national-candied-orange-peel-day-may-4.png", 
  "September 9,Wienerschnitzel Day": "http://wac.450f.edgecastcdn.net/80450F/b93.net/files/2015/09/Wienerschnitzel.jpg", 
  "January 5,National Whipped Cream Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/national-whipped-cream-day-jan-5.png", 
  "Last Thursday of June,National Bomb Pop Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/national-bomb-pop-day-last-thursday-in-june.png?w=300", 
  "November 4,National Candy Day": "https://nationaldaycalendar.com/wp-content/uploads/2014/06/National-Candy-Day-November-4-1024x512.jpg", 
  "September 15,National Linguine Day": "https://i0.wp.com/www.nationaldaycalendar.com/wp-content/uploads/2014/09/linguine.jpg?fit=1200%2C824&ssl=1&w=640"
}''')

DATA_URL = "https://en.wikipedia.org/wiki/List_of_food_days"
SECRETS_FILE = '.secrets'

def load_secrets():
  with open(SECRETS_FILE, 'r') as f:
    secrets = json.load(f)
  return secrets

def get_food_image(date, food_day):
  """
  Google image search - 100 searches per day.
  https://developers.google.com/image-search/
  """
  secrets = load_secrets()
  url = 'https://www.googleapis.com/customsearch/v1?num=1&start=1&searchType=image&imgSize=xlarge&q=%s&cx=%s&key=%s' % (food_day, secrets['cx'], secrets['key'])
  res = requests.get(url)
  if res.status_code != 200:
    print "%s,%s returned:" % (date, food_day)
    print res
  else:
    first_res = res.json()['items'][0]
    image_url = first_res['link']
    width = int(first_res['image']['width'])
    height = int(first_res['image']['height'])
    if width and height:
      return image_url
  return None

def load_info():
  new_img_cache = dict((key, value) for key, value in img_cache.items() if value is not None)
  for date in cache:
    for day in cache[date]:
      key = ",".join([date, day])
      if key not in new_img_cache:
        result = get_food_image(date, day)
        new_img_cache[key] = result
  print json.dumps(new_img_cache)

def generate_picture_table():
  res = u"<html><body><table border=\"1\"><tr><th>Date</th><th>Day</th><th>Image</th></tr>"
  for key, src in sorted(img_cache.items()):
    date, day = key.split(',', 1)
    res += "<tr><td>%s</td><td>%s</td><td><img src=\"%s\"/ height=\"100\" width=\"100\"></td></tr>" % (date, day, src)
  res += "</table></body></html>"
  with open('test.html', 'wb') as f:
    f.write(res.encode('utf-8'))

#load_info()
#generate_picture_table()

# Old functions written in JS, originally was going to make the requests on the fly, but decided
# it would be too slow and less reliable. Also, most of it is duplicated by https://github.com/ihurrahi/shouldipigout
"""
function addRowData(storage, date, day) {
  if (date in storage) {
    storage[date].push(day);
  } else {
    storage[date] = [day];
  }
}

function getRawData(callback) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", DATA_URL);
  xhr.onload = function() {
    var result = this.responseText;
    var el = document.createElement('html');
    el.innerHTML = result;
    allContent = el.getElementsByClassName('mw-body-content');
    var res = {};
    for (var i = 0; i < allContent.length; i++) {
      content = allContent[i];
      for (var j = 0; j < content.children.length; j++) {
        var child = content.children[j];
        if (child.innerHTML.includes('United States')) {
          usSection = false;
          for (var k = 0; k < child.children.length; k++) {
            var grandchild = child.children[k];
            if (grandchild.tagName == 'H2') {
              if (grandchild.innerText.includes('United States')) {
                usSection = true;
              } else {
                usSection = false;
              }
            }
            if (usSection) {
              if (grandchild.tagName == 'H3') {
                currentMonth = grandchild.getElementsByTagName('span')[0].innerText;
              } else if (grandchild.tagName == 'TABLE') {
                rows = grandchild.getElementsByTagName('tr');
                for (var l = 0; l < rows.length; l++) {
                  row = rows[l];
                  rowData = row.getElementsByTagName('td');
                  if (rowData.length > 0) {
                    date = rowData[0].innerText;
                    monthFound = false;
                    for (var x = 0; x < MONTHS.length; x++) {
                      if (date.includes(MONTHS[x])) {
                        monthFound = true;
                      }
                    }
                    if (!(monthFound)) {
                      date = date + " of " + currentMonth;
                    }
                    addRowData(res, date, rowData[1].innerText);
                  }
                }
              }
            }
          }
        }
      }
    }
    callback(res);
  }
  xhr.onerror = function() {
    console.log('Encountered network error while getting raw data.');
    callback('');
  }
  xhr.send();
}
"""
