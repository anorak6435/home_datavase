inv_location:
    PK(id)  : int
    name    : str
    description : str
    pos     : (int, int)
    size id : int

item_type:
    PK(id)  : int
    name    : str

inv_item:
    id      : int
    name    : str
    item_type id : int
    description : str
    size id : int
    inv_location id : int

size:
    PK(id)  : int
    name    : str
    length  : int
    width   : int
    height  : int
