using Gadfly

vel = collect(0:340)
Temp = collect(273:323)
M = Float64[]


function MachNumber(v,T)
  R = 287.058 #Rstar = R/M
  P = 100 #Pa
  γ = 1.4
  ρ = (P/(R*T))
  a = sqrt((γ*P)/ρ)
  Mach = v/a
  return Mach
end
