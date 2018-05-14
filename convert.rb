open("ruby3","w") do |fe|
open(ARGV[0]) do |f|
  while (name = f.readlines)
    name.sort!
    str = name.join(', ')
    p str.chomp!
    name.each do |n|
    #fe.print n.split('/')
    end
    exit!
 end
end
end