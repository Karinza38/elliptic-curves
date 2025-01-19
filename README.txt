 elliptic-curves
===============
Play with elliptic curves!
A senior thesis project, Fall 2014 - Spring 2015.

Terms:
ECDLP = elliptic curve discrete log problem

   setup.py
   To install package, download the folder, then navigate to (outer) primecurves 
   directory in the command prompt. Type:
      python setup.py install
   Then, if you want to edit on your computer (and have changes show up) type:
      python setup.py develop
      
-- /latex
   The written part of my thesis.

-- /primecurves
   PYTHON VERSION: 2.7.6
   A python package. All things related to elliptic curves over prime fields (Z/pZ).
   
   Structures:
      PrimeCurve        - elliptic curve
      PrimePoint        - point on an elliptic curve
      PrimeFieldElement - element of a prime field F_p, i.e., an integer mod p
      PAdic             - p-adic rational number (in Q_p)       // TODO!
      Weierstrass       - Weierstrass form of an elliptic curve, used to compute lifts
      
   Algorithms:
      bruteforcelog     - compute ECDLP by brute force (enumeration)
      pollardsrho       - compute ECDLP by Pollard's rho algorithm - more TODO
                          (currently only an implementation for Z/pZ)
      traceone          - compute ECDLP on curves of trace one  // TODO!
      
   Other stuff:
      numbertheory      - a few helpful algorithms from number theory: 
                          gcd, successive squaring, etc.
      turtlevisuals     - visualize elliptic curves over prime fields using 
                          Python's Turtle graphics.

   -- /images
      Contains screenshots and other visuals.
      
      
      
      
      
