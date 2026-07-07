# Q.1 current_actions = ["line", "circle", "square"]
# backup_actions = current_actions
# current_actions.append("triangle")

# If you print backup_actions, will it contain "triangle" or not? Explain what happens in Python's memory behind this behavior.
# current_actions = ["line", "circle", "square"]
# backup_actions = current_actions
# current_actions.append("triangle")

# print(backup_actions)

# Q.2 E-Commerce Cart Slicing
# cart = ["shoes", "shirt", "watch", "hat", "belt", "socks"]
# update_cart = cart[-3:]
# print(update_cart)

# Q.3 Inventory Sorting & Case Sensitivity
# A warehouse management system runs .sort() on a list of product tags: tags = ["banana", "Vipia", "apple", "cherry", "vipin"]. Write down exactly what the list will look like after running tags.sort(), and explain how capital letters affect the sorting order.

# tags = ["banana", "Vipia", "apple", "cherry", "vipin"]
# tags.sort()
# print(tags)

# Q.4 IoT Sensor Data Extraction (Slicing with Steps)
# An industrial IoT sensor records temperatures every single minute of an hour, resulting in a list of 60 items. You want to downsample this data to look at every 4th minute's reading. Given a list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], write a slice expression that retrieves every 4th element starting from index 0.

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = numbers[::4]
# print(result)

# # Q.5 Social Media App Notification Feed
# A user's notification feed is a list of strings. When a new notification arrives, it needs to be pushed to the very top (index 0) of their feed, pushing everything else down. Given notifications = ["Like", "Comment"], write the exact code to add "New Follower" to the beginning of the list using a position-based list method.

# notifications = ["Like", "Comment"]
# notifications.insert(0, "New Follower")
# print(notifications)

#  Q.6 Banking Ledger: Appending vs. Extending Batch Transactions
 # A banking app has an active transaction ledger: ledger = [100, -50, 200]. A batch of new external transactions arrives as a sublist: new_batch = [500, -20, 30].
  # Predict what ledger will look like if you use ledger.append(new_batch).
  # Predict what ledger will look like if you use ledger.extend(new_batch) instead.

# ledger = [100, -50, 200]
# new_batch = [500, -20, 30]
# ledger.append(new_batch)
# print(ledger)


ledger = [100, -50, 200]
new_batch = [500, -20, 30]
ledger.extend(new_batch)
print(ledger)