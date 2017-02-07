def data_type(argumento):
  if type(argumento) == str:
    return len(argumento)
    
  if argumento is None:
    return 'no value'
    
  if type(argumento) == bool:
    return argumento
    
  if type(argumento) == int:
    if argumento < 100:
      return 'less than 100'
    elif argumento == 100:
      return 'equal to 100'
    else:
      return 'more than 100'
      
  if type(argumento) == list:
    if len(argumento) >= 3:
      return argumento[2]
    else:
      return None
    
  
    