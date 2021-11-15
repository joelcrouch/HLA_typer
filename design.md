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
 

   

