# The HLA TYPER: Design
Joel Crouch 2021

## Introduction

This document describes the architecture of this program.

## Architecture
How will this work?
Requirements:  Need a type from the donor, with associated transplant bank data describing the donor (id, weight,
ABO, social requirements(drug use ect), age, C.O.D., DCD vs BD (deceased vs brain death).
In order to proceed after that, donor data needs to be input and a match run ran by the transplant bank.
UNOS, and the surgeons will provide the match data-which patients to run against.  
Run a virtual crossmatch.  If the patients on the list have an expired ID or only one, run an ID to confirm antibodies 
have not changed.  
How to rule out:  If the patient produces AB's to the donor sera (virtual or real cxmatch), they are ruled out.
Also must be ABO and size matched.  Recipients may also have some requirements, not related to genotype.

Pt's on the waitlist (read:  in house data base) will be genotyped, at least with the A, B, and DR antigens.  Most likely have a DQ as well.
Have to address alpha/beta strings as well.

So here is an idea of the data in the waitlist(wl).
Name and associated data-address, phone number
Doctor data(who is the nephrologist, primary care, nurse coordinator)
Hospital system (if applicable) for example: OHSU vs. VA vs Legacy vs Kaiser
Dialysis Center
dob
cod
weight
Medical data
 antibodies produced
 genotype (A,B,DR,DQ,C)
 social data -will take any kidney etc?
 cross match data?
 what organ(s) do they need?
 

   

