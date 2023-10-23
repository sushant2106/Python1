import re

# pattern="is"
# txt='''
# In meteorology, a cyclone ahello  large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.[6] Upper level cyclones can exist without the presence of a surface low, and can pinch off from the base of the tropical upper tropospheric trough during the summer months in the Northern Hemisphere. Cyclones have also been seen on extraterrestrial planets, such as Mars, Jupiter, and Neptune.[7][8] Cyclogenesis is the process of cyclone formation and intensification.[9] Extratropical cyclones begin as waves in large regions of enhanced mid-latitude temperature contrasts called baroclinic zones. These zones contract and form weather fronts as the cyclonic circulation closes and intensifies. Later in their life cycle, extratropical cyclones occlude as cold air masses undercut the warmer air and become cold core systems.
#  A cyclone's track is guided  over mhello the course of its 2 to 6 day life cycle by the steering flow of the subtropical jet stream.
# '''
# match=re.search(pattern,txt)
# print(match.span())

# x=re.findall("[A-M]",txt)
# print(x)

# y=re.findall("^hello",txt)
# print(y)



# pattern2="[a-z]hello"

# z=re.search(pattern2,txt) #it will return  first match
# print(z)

# m=re.findall(pattern2,txt) #it will return  
# print(m) # finditer


# txt2="this is 59 dollar  tams"
# s=re.findall("\d",txt2)
# print(s)

# k=re.findall("t..s",txt2) # start with t and end with s and any two character bw them
# print(k)


str1 = "Emma's luck numbers are 251 761 231 451"
# pattern to find three consecutive digits
string_pattern=r"\d{3}"
regex_pattern=re.compile(string_pattern)

result=regex_pattern.findall(str1)
print(result)
str2 = "Kelly's luck numbers are 111 212 415"
print(regex_pattern.findall(str2))

#search start with l and end with k ans no of sequence is zero or more in between them
print(re.findall("l.*k",str1))
