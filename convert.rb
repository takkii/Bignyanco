open("ruby_complete","w+") do |fe|
open(ARGV[0]) do |f|
  while (name = f.readlines)
    name.sort!
    str = name.join(', ')
    str.chomp!
    name.each do |n|
    fe.print n.split('/')
    three = ',"]'
    four = '",'
    five = '["'
    six = '"'
    fe.write n.read.gsub(/#{three}/,four)
    fe.write n.read.gsub(/#{five}/,six)
    f.close
    fe.close
    n.close
    end
    exit!
  end
  end
end
