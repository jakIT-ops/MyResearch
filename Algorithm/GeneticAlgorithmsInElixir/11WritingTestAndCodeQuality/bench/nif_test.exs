defmodule NifTest do
  alias Types.Chromosome
  def single_point_nif(p1, p2) do
    cx_point = rem(Genetic.xor96(), p1.size)
    {p1_head, p1_tail} = Enum.split(p1.genes, cx_point)
    {p2_head, p2_tail} = Enum.split(p2.genes, cx_point)
    {c1, c2} = {p1_head ++ p2_tail, p2_head ++ p1_tail}
    {%Chromosome{genes: c1, size: length(c1)},
      %Chromosome{genes: c2, size: length(c2)}}
  end

  def single_point_regular(p1, p2) do
    cx_point = :rand.uniform(p1.size)
    {p1_head, p1_tail} = Enum.split(p1.genes, cx_point)
    {p2_head, p2_tail} = Enum.split(p2.genes, cx_point)
    {c1, c2} = {p1_head ++ p2_tail, p2_head ++ p1_tail}
    {%Chromosome{genes: c1, size: length(c1)},
      %Chromosome{genes: c2, size: length(c2)}}
  end
end

genes = for x <- 1..1000, do: x

c1 = %Types.Chromosome{genes: genes, size: 1000}
c2 = %Types.Chromosome{genes: genes, size: 1000}

Benchee.run(%{
  "xor96 single point" => fn -> NifTest.single_point_nif(c1, c2) end,
  "regular single point" => fn -> NifTest.single_point_regular(c1, c2) end
  }, memory_time: 2)
