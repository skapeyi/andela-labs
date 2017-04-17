def replicate_iter(times, data):
	result = []
	if(isinstance(data,list) or isinstance(data,dict)) or (isinstance(times,list) or isinstance(times,dict)):
		raise ValueError
	if times == 0:
		return result

	if times < 0:
		return result	

	for i in range(0,times):
		result.append(data)

	return result


def replicate_recur(times, data):	
    if(isinstance(data,list) or isinstance(data,dict)) or (isinstance(times,list) or isinstance(times,dict)):
    	raise ValueError
    elif(times <= 0):
    	return []
    else:
    	return ([data] + replicate_recur((times - 1), data))  


replicate_recur(3,5)