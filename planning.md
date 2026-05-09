# Planning Document

## InventoryItem Class

### __init__()
Input:
- name
- quantity
- usage history

Output:
- creates inventory item object

Purpose:
Stores item information.

---

### burn_rate
Input:
- usage history

Output:
- average usage rate

Purpose:
Calculates average item usage over time.

---

### predict_depletion()
Input:
- quantity
- burn rate

Output:
- estimated remaining days

Purpose:
Predicts when inventory will reach zero.

---

## InventoryManager Class

### load_inventory()
Input:
- JSON file

Output:
- inventory list

Purpose:
Loads saved inventory data.

---

### save_inventory()
Input:
- inventory list

Output:
- JSON file

Purpose:
Saves inventory data permanently.

---

### add_item()
Input:
- item information

Output:
- updated inventory

Purpose:
Adds item and sorts inventory.

---

### merge_sort()
Input:
- unsorted inventory list

Output:
- sorted inventory list

Purpose:
Recursively sorts inventory alphabetically.

---

### search_item()
Input:
- item name

Output:
- matching item information

Purpose:
Uses binary search to find items quickly.
