
# NeopetShuffles
code for hosting Neopets UC pet trading shuffles

Basic Info:

shuffle.py - name of this script

listings.txt - where you will have the entries copy pasted from the neoboards

hostingPage.html - where the hosting page code will be written to

htmlVariables.py - the boilerplate HTML formatting I use, feel free to replace it with your own version

accepts.txt - where you will have the acceptances (and passes) copy pasted from the neoboards


Instructions
1. In your terminal, make sure you have python3 installed
2. Git clone this project
3. You will first have to manually copy paste Listings from the neoboards into the listings.txt file
4. Then to run the code use the command
```
python3 shuffle.py listings.txt
```
this will write all your boilerplate HTML as well as the listings into the hostingPage.html file

5. You may then copy the entirety of the hostingPage.html file onto whichever Pet Page you are using to host the shuffle
6. At the end of the shuffle to track acceptances you will have to manually copy paste acceptances into the accepts.txt file
7. Then to update your hostingPage.html file with acceptances you will run 
```
python3 shuffle.py listings.txt accepts.txt missing
```
which as of now will output the acceptances text into your terminal and display the missing pets as well
8. You then manually update the hostingPage.html Listings portion with the new text

TODO
1. Add the code to systematically update the host page wtih acceptances rather than manually copy pasting
2. Clean up Readme with nicer formatting

Examples:

a sample listing
```
Listing
 
Xxxx - UC Faerie Xwee (T6)
 
Quiggled pls
 
@maria
 
Listing
Xxxxxxx - UC Mallow (T2) QUIGGLE
@maylie
```

will output into the Listings portion
```
<br>
<br> 
 
Xxxxxxx - UC Mallow (T2) QUIGGLE
 
<br>
 
<br> 
 
Xxxx - UC Faerie Xwee (T6)
 
<br>
```
 and output into the Usernames portion

```
<br>
<br> 
 
@maria
 
<br>
 
<br> 
 
@maylie
 
<br>
```

When you are ready to update with acceptances run the following

```
python3 shuffle.py listings.txt accepts.txt missing
```




credits to neopets user: kougras_paw_brasil! a collaborative effort as she did most of the foundation building and heavy lifting and I add bonus features here and there!	



