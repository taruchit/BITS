prolongWaterSource:-
    catch(
        (
            writeln('Welcome to the Water Source Expert System'),
            getRainfall(Rainfall),
            getAquifer(Aquifer),
            getRiverDistance(RiverDistance),
            getLakeDistance(LakeDistance),
            getBeachDistance(BeachDistance),
            determineWaterSource(Rainfall, Aquifer, RiverDistance, LakeDistance, BeachDistance, Water),
            writeln(''),
            format('The suitable water source is: ~w', [Water])
        ),
        E,
        (
            format('An error occurred: ~w', [E]),
            fail
        )
    ).
    
getRainfall(Rainfall) :-
    writeln('Enter rainfall intensity in (mm/month): '),
    read(Temp),
    ( number(Temp) -> Rainfall = Temp ; writeln('Invalid input. Rainfall intensity must be a number.'), getRainfall(Rainfall) ).

getAquifer(Aquifer) :-
    writeln('Enter type of aquifer in (sandy/other): '),
    read(Temp),
    ( member(Temp, [sandy, other]) -> Aquifer = Temp ; writeln('Invalid input. Aquifer type must be sandy or other.'), getAquifer(Aquifer) ).

getRiverDistance(RiverDistance) :-
    writeln('Enter distance from river in (km): '),
    read(Temp),
    ( number(Temp) -> RiverDistance = Temp ; writeln('Invalid input. Distance from river must be a number.'), getRiverDistance(RiverDistance) ).

getLakeDistance(LakeDistance) :-
    writeln('Enter distance from lake in (km): '),
    read(Temp),
    ( number(Temp) -> LakeDistance = Temp ; writeln('Invalid input. Distance from lake must be a number.'), getLakeDistance(LakeDistance) ).

getBeachDistance(BeachDistance) :-
    writeln('Enter distance from beach in (km): '),
    read(Temp),
    ( number(Temp) -> BeachDistance = Temp ; writeln('Invalid input. Distance from beach must be a number.'), getBeachDistance(BeachDistance) ).



determineWaterSource(Rainfall, Aquifer, RiverDistance, LakeDistance, BeachDistance, Water) :-
    (
        LakeDistance < 10 -> Water = lake; 
        RiverDistance < 8, Rainfall >= 200 ->  Water = rain; 
        RiverDistance < 8, Rainfall < 200 ->  Water = river;
        Rainfall >= 150 -> Water = rain; 
        Aquifer \= sandy, LakeDistance < 14 ->  Water = lake; 
        Aquifer \= sandy, LakeDistance >= 14 ->  Water = rain;
        BeachDistance >= 5 ->  Water = groundwater;
        RiverDistance < 20 -> Water = river;
        RiverDistance >= 20 -> Water = rain
    ).


