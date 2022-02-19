package com.learning.enums;

import java.util.EnumSet;

@FunctionalInterface
interface Type{
    Boolean isValidValue(String s);
    default Boolean isValidValue2(String s){ // We can have a default method inside a interface , TODO usecase?
        return true;
    }
}

enum DataType{

    BOOLEAN(val->val=="true" || val=="false"),
    STRING(val->val.length() != 0);

    private Type typeLambda;


    DataType(Type typeLambda){
        this.typeLambda = typeLambda;
    }


    public Boolean isValidValue(String s){
        return this.typeLambda.isValidValue(s);
    }
}

public class StrategyPatternUsingEnum {
    public static void main(String args[]) {

        for(DataType d: DataType.values()){

            System.out.println(d.name());
        }

        for(DataType d: EnumSet.range(DataType.BOOLEAN,DataType.STRING)){
            System.out.println(d.ordinal());
            System.out.println(d.isValidValue(""));
        }
    }
}