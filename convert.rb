open("ruby_complete","w+") do |fe|
open(ARGV[0]) do |f|
  while (name = f.readlines)
    name.sort!
    str = name.join(', ')
    str.chomp!
    name.each do |n|
    fe.write n.read.gsub(',"]','",')
    fe.write n.read.gsub('["','"')
    f.close
    fe.close
    end
    exit!
  end
  end
end
