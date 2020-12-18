# GC-content
This app analyzes GC content all over genomes
This application calculates and creates a graphical visualization of a genome's GC content.
First it asks you to import a text or fna file (Fasta files usually have the fna format). This is case sensitive.
Then you have to define the window size, meaning the number of bases, you want your window to have. 
Please not that this is not a rolling window, and there is no overlaps, eg. ATCTTG, window size=3, creates ATC and TTG, and not rolling window of type ATC,TCT,CTT,TTG.
Then it asks you to enter you Standard Deviation (SD) margins of your choice , this is closely related to the degree of certainty of your final results. Eg for SD=2 you get results with a 5% confidence rate.
From this point on the code may take several seconds or minutes to run especially if you entered a large genome.
You get a plot of base position and GC content, the dashed blue lines are the margins based on your SD, and dashed black line is the mean of obesrvations. You can save this to your computer. 
Then close this plot window and then another window shows up which shows the weighted AT , the form of this graph determines whether you have  genome whose replication starting point is a single area (this is the case if you notice a noticable change of pattern  where the mean of the left part of the graph and the mean on the right part of the graph differ substantially). If your genome has multiple possible replication starting points you will not notice any change of pattern.
The program extracts on your terminal the positions on the genome with the high GC content and on the window that shows up you press Y , if you want it to extract the actual areas and in that case you will get the DNA sequences with a name of your choice on your working directory.

Copyright @ P.Kyres 2020
