import re
import os.path
import string
from .base import Base
import traceback

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'Nekodaruma2'
        self.filetypes = ['ruby']
        self.mark = '[neko_dictionary]'
        self.rank = 500
        self.input_pattern = r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*'
        
    def get_complete_position(self, context):
        m = re.search(r'[^. *\t]\w*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try
        fi = ["!","!=","!=","!~","!~","**","+@","-@","<","<<","<=","<=","<=>","<=>","==","==","===","===","=~","=~",">",">=",">=",">>","ALT_SEPARATOR","ANSI_X3_4_1968","ARGF","ARGV","ASCII","ASCII_8BIT","AUTO","Acceptables","AmbiguousArgument","AmbiguousOption","Arguable","ArgumentError","ArgumentStyle","Array","Assertion","Assertions","BENCHMARK_VERSION","BIG5","BIG5_HKSCS","BIG5_HKSCS_2008","BIG5_UAO","BINARY","Backtrace","BacktraceFilter","BasicObject","Benchmark","Big5","Big5_HKSCS","Big5_HKSCS_2008","Big5_UAO","Bignum","Binding","CAPTION","COMPSYS_HEADER","CONFIG","CP1250","CP1251","CP1252","CP1253","CP1254","CP1255","CP1256","CP1257","CP1258","CP437","CP50220","CP50221","CP51932","CP65000","CP65001","CP737","CP775","CP850","CP852","CP855","CP857","CP860","CP861","CP862","CP863","CP864","CP865","CP866","CP869","CP874","CP878","CP932","CP936","CP949","CP950","CP951","CROSS_COMPILING","CSWINDOWS31J","Class","CommandLineError","Comparable","CompatibilityError","CompletingHash","Completion","Complex","ConditionVariable","Config","ConfigFile","ConfigMap","Constants","Converter","ConverterNotFoundError","CsWindows31J","DEFAULT","DEFAULT_HOST","DEFAULT_PARAMS","DESTDIR","DIG","DRb::DRbBadScheme","DRb::DRbBadURI","DRb::DRbConnError","DRb::DRbError","DRb::DRbIdConv","DRb::DRbIdConv","DRb::DRbObject","DRb::DRbObject","DRb::DRbObservable","DRb::DRbProtocol","DRb::DRbRemoteError","DRb::DRbServer","DRb::DRbServerNotFound","DRb::DRbUndumped","DRb::DRbUndumped","DRb::DRbUnknown","DRb::DRbUnknown","DRb::DRbUnknownError","DRb::ExtServ","DRb::ExtServManager","DRbIdConv","DRbObject","DRbUndumped","Data","Date","DateTime","DateTime.now.strftime("%Y-%m-%d %H:%M:%S")","DateTime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")","DecimalInteger","DecimalNumeric","Default","DefaultList","Dependency","DependencyError","DependencyList","DependencyRemovalException","DependencyResolver","Deprecate","Dir","DocumentError","DomainError","E2BIG","EACCES","EADDRINUSE","EADDRNOTAVAIL","EADV","EAFNOSUPPORT","EAGAIN","EALREADY","EAUTH","EBADE","EBADF","EBADFD","EBADMSG","EBADR","EBADRPC","EBADRQC","EBADSLT","EBFONT","EBUSY","ECANCELED","ECHILD","ECHRNG","ECOMM","ECONNABORTED","ECONNREFUSED","ECONNRESET","EDEADLK","EDEADLOCK","EDESTADDRREQ","EDOM","EDOOFUS","EDOTDOT","EDQUOT","EEXIST","EFAULT","EFBIG","EFTYPE","EHOSTDOWN","EHOSTUNREACH","EIDRM","EILSEQ","EINPROGRESS","EINTR","EINVAL","EIO","EIPSEC","EISCONN","EISDIR","EISNAM","EKEYEXPIRED","EKEYREJECTED","EKEYREVOKED","EL2HLT","EL2NSYNC","EL3HLT","EL3RST","ELIBACC","ELIBBAD","ELIBEXEC","ELIBMAX","ELIBSCN","ELNRNG","ELOOP","EMACS_MULE","EMEDIUMTYPE","EMFILE","EMLINK","EMSGSIZE","EMULTIHOP","ENAMETOOLONG","ENAVAIL","ENEEDAUTH","ENETDOWN","ENETRESET","ENETUNREACH","ENFILE","ENOANO","ENOATTR","ENOBUFS","ENOCSI","ENODATA","ENODEV","ENOENT","ENOEXEC","ENOKEY","ENOLCK","ENOLINK","ENOMEDIUM","ENOMEM","ENOMSG","ENONET","ENOPKG","ENOPROTOOPT","ENOSPC","ENOSR","ENOSTR","ENOSYS","ENOTBLK","ENOTCONN","ENOTDIR","ENOTEMPTY","ENOTNAM","ENOTRECOVERABLE","ENOTSOCK","ENOTSUP","ENOTTY","ENOTUNIQ","ENV","ENXIO","EOFError","EOPNOTSUPP","EOVERFLOW","EOWNERDEAD","EPERM","EPFNOSUPPORT","EPIPE","EPROCLIM","EPROCUNAVAIL","EPROGMISMATCH","EPROGUNAVAIL","EPROTO","EPROTONOSUPPORT","EPROTOTYPE","EPSILON","ERANGE","EREMCHG","EREMOTE","EREMOTEIO","ERESTART","ERFKILL","EROFS","ERPCMISMATCH","ESHUTDOWN","ESOCKTNOSUPPORT","ESPIPE","ESRCH","ESRMNT","ESTALE","ESTRPIPE","ETIME","ETIMEDOUT","ETOOMANYREFS","ETXTBSY","EUC","EUCCN","EUCJP","EUCJP_MS","EUCKR","EUCLEAN","EUCTW","EUC_CN","EUC_JISX0213","EUC_JP","EUC_JP_2004","EUC_JP_MS","EUC_KR","EUC_TW","EUNATCH","EUSERS","EWOULDBLOCK","EXDEV","EXFULL","EXTENDED","Emacs_Mule","Encoding","EncodingError","EndOfYAMLException","Enumerable","Enumerator","Env","Errno","ErrorReason","EucCN","EucJP","EucJP_ms","EucKR","EucTW","Exception","FALSE","FIXEDENCODING","FORMAT","FalseClass","Fiber","FiberError","File","FilePermissionError","FileTest","Fixnum","Float","FloatDomainError","FormatException","GB12345","GB18030","GB1988","GBK","GC","GEM_DEP_FILES","GEM_PRELUDE_SUCKAGE","GID","Gem","GemNotFoundException","GemNotInHomeException","Generator","Hash","IBM437","IBM737","IBM775","IBM850","IBM852","IBM855","IBM857","IBM860","IBM861","IBM862","IBM863","IBM864","IBM865","IBM866","IBM869","IGNORECASE","INFINITY","INSTRUCTION_NAMES","IO","IOError","ISO2022_JP","ISO2022_JP2","ISO8859_1","ISO8859_10","ISO8859_11","ISO8859_13","ISO8859_14","ISO8859_15","ISO8859_16","ISO8859_2","ISO8859_3","ISO8859_4","ISO8859_5","ISO8859_6","ISO8859_7","ISO8859_8","ISO8859_9","ISO_2022_JP","ISO_2022_JP_2","ISO_2022_JP_KDDI","ISO_8859_1","ISO_8859_10","ISO_8859_11","ISO_8859_13","ISO_8859_14","ISO_8859_15","ISO_8859_16","ISO_8859_2","ISO_8859_3","ISO_8859_4","ISO_8859_5","ISO_8859_6","ISO_8859_7","ISO_8859_8","ISO_8859_9","IndexError","InstallError","InstructionSequence","Integer","Interrupt","InvalidArgument","InvalidByteSequenceError","InvalidOption","InvalidSpecificationException","JIS","Job","KOI8_R","KOI8_U","Kernel","KeyError","LastModified","Lazy","List","LoadError","LocalJumpError","MACCENTEURO","MACCROATIAN","MACCYRILLIC","MACGREEK","MACICELAND","MACJAPAN","MACJAPANESE","MACROMAN","MACROMANIA","MACTHAI","MACTURKISH","MACUKRAINE","MAJOR_VERSION","MAKEFILE_CONFIG","MANT_DIG","MARSHAL_SPEC_DIR","MAX","MAX_10_EXP","MAX_EXP","MIN","MINOR_VERSION","MIN_10_EXP","MIN_EXP","MULTILINE","MUTEX_FOR_THREAD_EXCLUSIVE","MacCentEuro","MacCroatian","MacCyrillic","MacGreek","MacIceland","MacJapan","MacJapanese","MacRoman","MacRomania","MacThai","MacTurkish","MacUkraine","Marshal","MatchData","Math","Method","MiniTest","Minitest","MissingArgument","Module","Mutex","NAN","NIL","NKF","NKF_RELEASE_DATE","NKF_VERSION","NOCONV","NOENCODING","NOERROR","NO_ARGUMENT","NameError","NeedlessArgument","NilClass","NoArgument","NoMemoryError","NoMethodError","NotImplementedError","Numeric","OPTIONAL_ARGUMENT","OPTS","Object","Object","ObjectSpace","OctalInteger","Officious","OperationNotSupportedError","OptionMap","OptionParser","OptionalArgument","PATH_SEPARATOR","PCK","PI","ParallelEach","ParseError","PathSupport","Platform","PlatformMismatch","Proc","Process","Profiler","Queue","RADIX","RCSID","REPOSITORY_SUBDIRECTORIES","REQUIRED_ARGUMENT","ROUNDS","RUBYGEMS_DIR","RUBY_COPYRIGHT","RUBY_DESCRIPTION","RUBY_ENGINE","RUBY_PATCHLEVEL","RUBY_PLATFORM","RUBY_RELEASE_DATE","RUBY_REVISION","RUBY_VERSION","Random","Range","RangeError","Rational","RbConfig","RbConfigPriorities","Regexp","RegexpError","Release","RemoteError","RemoteInstallationCancelled","RemoteInstallationSkipped","RemoteSourceException","Report","RequestSet","RequiredArgument","Requirement","RubyGemsPackageVersion","RubyGemsVersion","RubyVM","RuntimeError","SEEK_CUR","SEEK_END","SEEK_SET","SEPARATOR","SHIFT_JIS","SJIS","SJIS_DOCOMO","SJIS_DoCoMo","SJIS_KDDI","SJIS_SOFTBANK","SJIS_SoftBank","SPLAT_PROC","STATELESS_ISO_2022_JP","STATELESS_ISO_2022_JP_KDDI","STDERR","STDIN","STDOUT","ScriptError","SecurityError","Separator","Shift_JIS","Signal","SignalException","SizedQueue","Skip","Source","SourceFetchProblem","SourceList","SpecFetcher","SpecificGemNotFoundException","Specification","StandardError","Stat","Stateless_ISO_2022_JP","Stateless_ISO_2022_JP_KDDI","Status","StopIteration","String","Struct","Switch","Symbol","SyntaxError","Sys","SystemCallError","SystemExit","SystemExitException","SystemStackError","TIS_620","TOPDIR","TOPLEVEL_BINDING","TRUE","Thread","ThreadError","ThreadGroup","Time","Tms","TracePoint","TrueClass","TypeError","UCS_2BE","UCS_4BE","UCS_4LE","UID","UNKNOWN","US_ASCII","UTF16","UTF32","UTF8","UTF8_DOCOMO","UTF8_DoCoMo","UTF8_KDDI","UTF8_MAC","UTF8_SOFTBANK","UTF8_SoftBank","UTF_16","UTF_16BE","UTF_16LE","UTF_32","UTF_32BE","UTF_32LE","UTF_7","UTF_8","UTF_8_HFS","UTF_8_MAC","UnboundMethod","UndefinedConversionError","Unit","VERSION","VerificationError","Version","WINDOWS_1250","WINDOWS_1251","WINDOWS_1252","WINDOWS_1253","WINDOWS_1254","WINDOWS_1255","WINDOWS_1256","WINDOWS_1257","WINDOWS_1258","WINDOWS_31J","WINDOWS_874","WIN_PATTERNS","WNOHANG","WUNTRACED","WaitReadable","WaitWritable","WeakMap","Windows_1250","Windows_1251","Windows_1252","Windows_1253","Windows_1254","Windows_1255","Windows_1256","Windows_1257","Windows_1258","Windows_31J","Windows_874","Yielder","ZeroDivisionError","]","]=","__END__","__callee__","__dir__","__id__","__id__","__method__","__send__","__send__","_deprecated_activate","_deprecated_activate_dep","_deprecated_activate_spec","_deprecated_all_load_paths","_deprecated_available?","_deprecated_cache","_deprecated_cache_dir","_deprecated_cache_gem","_deprecated_default_system_source_cache_dir","_deprecated_default_user_source_cache_dir","_deprecated_latest_load_paths","_deprecated_promote_load_path","_deprecated_required_location","_deprecated_searcher","_deprecated_source_index","_dump","_httpdate","_id2ref","_iso8601","_jisx0301","_load","_parse","_rfc2822","_rfc3339","_rfc822","_strptime","_warn_","_xmlschema","abort","abort_on_exception","abort_on_exception=","abs","abs2","absolute_path","accept","acos","acosh","activate","activate_dep","activate_spec","add","add_officious","add_trace_func","advise","ajd","alias","alias_method","alias_method","aliases","alive?","all?","all_load_paths","all_partials","all_symbols","allocate","allocate","amjd","ancestors","ancestors","and","angle","any?","append_features","arg","args","arity","ascii_compatible?","ascii_only?","asctime","asin","asinh","assoc","at","at_exit","atan","atan2","atanh","atime","attr","attr","attr_accessor","attr_accessor","attr_reader","attr_reader","attr_writer","attr_writer","autoclose=","autoclose?","autoload","autoload","autoload?","autoload?","available?","backtrace","backtrace_filter","backtrace_filter=","backtrace_locations","banner","banner=","base","basename","begin","benchmark","between?","bin_path","binary_mode","bind","binding","bindir","binmode","binmode?","binread","binwrite","block_given?","blockdev?","bm","bmbm","break","broadcast","bsearch","bytes","bytesize","byteslice","cache","cache_dir","cache_gem","call","caller","caller_locations","candidate","capitalize","capitalize!","captures","case","casecmp","casefold?","catch","cbrt","ceil","center","chardev?","chars","chdir","chmod","chomp","chomp!","chop","chop!","chown","chr","chroot","chunk","civil","class","class","class_eval","class_eval","class_exec","class_exec","class_variable_defined?","class_variable_defined?","class_variable_get","class_variable_get","class_variable_set","class_variable_set","class_variables","class_variables","clear","clear_default_specs","clear_paths","clone","clone","close","close_on_exec=","close_on_exec?","close_read","close_write","closed?","codepoints","coerce","collect","collect!","collect_concat","combination","commercial","compact","compact!","compare_by_identity","compare_by_identity?","compatible?","compile","compsys","concat","config_file","configuration","configuration=","conj","conjugate","const_defined?","const_defined?","const_get","const_get","const_missing","const_missing","const_set","const_set","constants","constants","copy_stream","cos","cosh","count","count_objects","cover?","crypt","ctime","current","curry","cwday","cweek","cwyear","cycle","daemon","datadir","day","day_fraction","def","def","def_head_option","def_option","def_tail_option","default","default=","default_argv","default_argv=","default_bindir","default_dir","default_exec_format","default_external","default_external=","default_internal","default_internal=","default_path","default_proc","default_proc=","default_rubygems_dirs","default_sources","default_system_source_cache_dir","default_user_source_cache_dir","define","define_finalizer","define_head","define_method","define_method","define_singleton_method","define_singleton_method","define_tail","defined?","defined_class","deflate","delete","delete!","delete_at","delete_if","denominator","deprecate_constant","deq","detach","detect","detect_gemdeps","dir","directory?","dirname","disable","display","display","div","divmod","do","done_installing","done_installing_hooks","downcase","downcase!","downto","drb", "acl","drb", "extserv","drb", "extservm","drb", "gw","drb", "observer","drb", "ssl","drb", "timeridconv","drb", "unix","drop","drop_while","dst?","dummy?","dump","dup","dup","each","each_byte","each_char","each_codepoint","each_cons","each_entry","each_index","each_key","each_line","each_object","each_pair","each_slice","each_value","each_with_index","each_with_object","egid","egid=","else","elsif","empty?","enable","enabled?","enclose","enclosed?","encode","encode!","encoding","end","end","end_with?","england","enq","ensure","ensure_gem_subdirectories","entries","enum_for","enum_for","environment","eof","eof?","eql?","eql?","equal?","equal?","erf","erfc","errno","escape","euid","euid=","eval","even?","event","exception","exclude_end?","exclusive","exec","executable?","executable_real?","exist?","exists?","exit","exit!","exit_value","exp","expand","expand_path","extend","extend","extend_object","extended","external_encoding","extname","fail","false","fcntl","fdatasync","fdiv","feed","fetch","file?","fileno","fill","filter_backtrace","find","find_all","find_files","find_index","find_unresolved_default_spec","finish_resolve","finite?","first","fixed_encoding?","flat_map","flatten","flatten!","flock","floor","flush","fnmatch","fnmatch?","for","for_fd","force_encoding","foreach","fork","format","freeze","freeze","frexp","friday?","frozen?","frozen?","fsync","ftype","fuga","gamma","garbage_collect","gcd","gcdlcm","gem","gem_original_require","getbyte","getc","getgm","getlocal","getopts","getpgid","getpgrp","getpriority","getrlimit","gets","getsid","getutc","getwd","gid","gid=","glob","global_variables","gm","gmt?","gmt_offset","gmtime","gmtoff","gregorian","gregorian?","gregorian_leap?","grep","group","group_by","groups","groups=","grpowned?","gsub","gsub!","guess","gunzip","gzip","handle_interrupt","has_key?","has_value?","hash","hash","help","hex","hoge","home","host","host=","hour","httpdate","hypot","id2name","identical?","if","imag","imaginary","in","inc","include","include","include?","include?","included","included_modules","included_modules","index","infinite?","inflate","inherited","initgroups","initialize","initialize_clone","initialize_copy","initialize_dup","inject","insert","inspect","inspect","install","instance_eval","instance_eval","instance_exec","instance_exec","instance_method","instance_method","instance_methods","instance_methods","instance_of?","instance_of?","instance_variable_defined?","instance_variable_defined?","instance_variable_get","instance_variable_get","instance_variable_set","instance_variable_set","instance_variables","instance_variables","integer?","intern","internal_encoding","invert","ioctl","is_a?","is_a?","isatty","isdst","iseuc","isjis","iso8601","issjis","isutf8","italy","iterator?","itself","jd","jisx0301","join","julian","julian?","julian_leap?","kconv","keep_if","key","key?","keys","kill","kind_of?","kind_of?","lambda","lambda?","last","last_match","latest_load_paths","latest_rubygems_version","latest_spec_for","latest_version_for","lazy","lchmod","lchown","lcm","ld","ldexp","leap?","length","lgamma","lineno","lineno=","lines","link","list","ljust","load","load_env_plugins","load_path_insert_index","load_plugin_files","load_plugins","load_yaml","loaded_path?","loaded_specs","local","local_variables","locale_charmap","localtime","location_of_caller","lock","locked?","log","log10","log2","loop","lstat","lstrip","lstrip!","magnitude","main","make_switch","map","map!","marshal_dump","marshal_load","marshal_version","match","max","max=","max_by","maxgroups","maxgroups=","mday","measure","member?","members","merge","merge!","message","method","method","method_added","method_defined?","method_defined?","method_id","method_missing","method_removed","method_undefined","methods","methods","min","min_by","minmax","minmax_by","minute","mjd","mkdir","mktime","module","module","module_eval","module_eval","module_exec","module_exec","module_function","module_function","modulo","mon","monday?","month","mtime","name","name","name_list","named_captures","names","nan?","needs","nesting","nesting","new","new","new_offset","new_seed","new_start","next","next!","next_day","next_month","next_values","next_year","nil","nil?","nil?","nkf","none?","nonzero?","not","now","nsec","num_waiting","numerator","object_id","object_id","oct","odd?","offset","on","on_head","on_tail","one?","open","options","or","ord","order","order!","ordinal","owned?","owner","pack","parameters","parse","parse!","partition","pass","path","path_separator","paths","paths=","peek","peek_values","pending_interrupt?","permutation","permute","permute!","phase","pid","pipe","pipe?","platforms","platforms=","polar","pop","popen","pos","pos=","post_build","post_build_hooks","post_install","post_install_hooks","post_match","post_reset","post_reset_hooks","post_uninstall","post_uninstall_hooks","pp","ppid","pre_install","pre_install_hooks","pre_match","pre_reset","pre_reset_hooks","pre_uninstall","pre_uninstall_hooks","pred","prefix","prepend","prepend","prev_day","prev_month","prev_year","print","printf","priority","priority=","private","private_class_method","private_class_method","private_constant","private_constant","private_instance_methods","private_instance_methods","private_method_defined?","private_method_defined?","private_methods","private_methods","proc","product","program_name","program_name=","promote_load_path","protected","protected_instance_methods","protected_instance_methods","protected_method_defined?","protected_method_defined?","protected_methods","protected_methods","public","public_class_method","public_class_method","public_constant","public_constant","public_instance_method","public_instance_method","public_instance_methods","public_instance_methods","public_method","public_method","public_method_defined?","public_method_defined?","public_methods","public_methods","public_send","public_send","push","putc","puts","pwd","quo","quote","raise","raised_exception","rand","rassoc","rationalize","read","read_binary","read_nonblock","readable?","readable_real?","readbyte","readchar","readline","readlines","readlink","readpartial","real","real?","realdirpath","realpath","realtime","reason","receiver","rect","rectangular","redo","reduce","refine","refresh","regexp","register_default_spec","rehash","reject","reject!","release","release=","remainder","remove","remove_class_variable","remove_class_variable","remove_const","remove_instance_variable","remove_instance_variable","remove_method","remove_method","remove_unresolved_default_spec","rename","reopen","repeated_combination","repeated_permutation","replace","replicate","report_activate_error","require","require_relative","required_location","rescue","respond_to?","respond_to?","respond_to_missing?","restore","result","resume","retry","return","return_value","reverse","reverse!","reverse_each","rewind","rfc2822","rfc3339","rfc822","rindex","rjust","rmdir","rotate","rotate!","round","rpartition","rstrip","rstrip!","ruby","ruby_engine","ruby_version","rubygems_version","run","safe_level","sample","saturday?","scan","searcher","sec","sec_fraction","second","second_fraction","seed","seek","select","select!","self","send","send","separator","set_backtrace","set_banner","set_encoding","set_program_name","set_summary_indent","set_summary_width","set_trace_func","setbyte","setgid?","setpgid","setpgrp","setpriority","setrlimit","setsid","setuid?","shift","shuffle","shuffle!","signal","signame","signm","signo","sin","singleton_class","singleton_class","singleton_class?","singleton_method","singleton_method_added","singleton_method_removed","singleton_method_undefined","singleton_methods","singleton_methods"]
        return fi
        except Exception:
        print ("raise Exception throw message.")
        traceback.print_exec()
