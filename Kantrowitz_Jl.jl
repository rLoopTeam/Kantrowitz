using Gadfly
using Plots

P = 100 #Pa
R = 287.058 #Rstar = R/M
vel = collect(1:340)
Temp = collect(263:323)
M = Array{Float64}(340, 60)


function MachNumber(v,T)
  γ = 1.4
  a = sqrt(γ*R*T)
  Mach = v/a
  return Mach
end

for i in 1:340
    for j in
        M[i][j] = MachNumber(vel[i], Temp[j])
    end
end

println(M)
