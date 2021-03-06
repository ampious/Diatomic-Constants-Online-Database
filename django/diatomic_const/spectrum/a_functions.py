# FUnctions
from __future__ import unicode_literals
from django.db import models
from data_management.models import Molecular_state,Reference_publication,Diatomic_constant,Preferred_set,Constant_type


# THis file makes list of all molecule types are here and types of constants
# Meaning: "cl.molecular_state.symbol"
# Meaning: "cl.const_type.symbol."
# Here: cl is all data from database


# 1. Finds all molecule symbols and constans types in 2 lists
def SymbolsAndConstants(printing=False):
    # Select everything from database
    all_data=Diatomic_constant.objects.all()

    #Prepare list for symbol
    molecules_list=[]
    #list for constant types
    const_types=[]
    for sample in all_data:
        # Get all symbols of molecules
        sym=sample.molecular_state.symbol
        if sym not in molecules_list:
            molecules_list.append(sym)
        # Get the all constant types in database
        a1=sample.constant_type.symbol
        if a1 not in const_types:
            const_types.append(a1)

    if printing==True:
        print "There are ",len(molecules_list)," molecules types in database"
        print "There are ",len(const_types)," types of constants"
    return molecules_list,const_types


def MoleculesTypes(printing=False):
    # Select everything from database
    all_data=Diatomic_constant.objects.all()

    #Prepare list for symbol
    molecules_list=[]
    for sample in all_data:
        # Get all symbols of molecules
        sym=sample.molecular_state.symbol
        if sym not in molecules_list:
            molecules_list.append(sym)
    if printing==True:
        print "There are ",len(molecules_list)," molecules types in database"
    return molecules_list

def ConstantsTypes(pr=False):
    all_data=Diatomic_constant.objects.all()
    const_types=[]
    for sample in all_data:
        # Get the all constant types in database
        a1=sample.constant_type.symbol
        if a1 not in const_types:
            const_types.append(a1)

    if pr==True:
        print ("There are ",len(const_types)," types of constants")

    return const_types


def testing_some_function(a,b):
    print(a+b)



# Function that takes name of molecule as argument and print all
# values of molecular_state class

def all_values(name):
    data=Diatomic_constant.objects.all()
    values=[]
    for i in data:
        if i.molecular_state.symbol==name:
            values.append(i)
            print(i)
