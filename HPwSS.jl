module HeatPumpWithStorageSystem

using JuMP,HiGHS
using CoolProp


abstract type EnergySystem end
struct HeatPumpStorageSerie <: EnergySystem end

export HeatPumpStorageSerie

abstract type SystemObjectiveType end
struct MinimizeCost <: SystemObjectiveType end
struct MinimizeEnergyCost <: SystemObjectiveType end

export MinimizeCost,MinimizeEnergyCost

dirname = joinpath(pwd(), "src", "refrigerantPropertys")
for file in readdir(dirname)
	include(joinpath(dirname, file))
end
dirname = joinpath(pwd(), "src", "systemModels")
for file in readdir(dirname)
	include(joinpath(dirname, file))
end

export generateSystemCoff,generateAndSolve

end # module HeatPumpWithStorageSystem
