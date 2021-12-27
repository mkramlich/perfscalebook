#!/usr/bin/env python3

items = [
"1. Do Nothing (why? math-wise is perfect: min possible latency, cpu, mem & infinitely scalable)",
"2. Do Very Little (why? broadstrokes is the next most perfect & efficient thing after Do Nothing)",
"3. Static Not Dynamic",
"4. Cached",
"5. Distributed",
"6. Parallelized",
"7. Asynchronous",
"8. Incremental",
"9. Step Minimization",
"10. Paginated Results",
"11. Complexity (in Time or Space) Cost Optimal Algorithms (eg. O(1) over O(n) over O(n^2))",
"12. Event-Driven not Polled",
"13. Non-Blocking IO",
"14. Web Page Component Request Minimization",
"15. Network Locality (eg. CDN’s)",
"16. Machine Task-to-Data Locality (eg. Hadoop)",
"17. Precompute Predicted Requests",
"18. Eager Init vs Lazy Init",
"19. Higher CPU Clock Speed",
"20. Higher CPU Core Count",
"21. CPU Instructions Which Do More Work Per Cycle/Tock (eg. SIMD)",
"22. Higher Communication Bus Speed, Throughput",
"23. Do Tasks in Hardware Rather than Software",
"24. Leaner Languages & Runtimes",
"25. More Memory",
"26. Faster Memory",
"27. More Disk/Storage",
"28. Faster Disk/Storage (Seek, Read, Write)",
"29. Disk/Storage Defragmentation",
"30. SSD not HDD (for random access latency)",
"31. Local Disk/Storage Rather Than Network Mounted",
"32. Higher Network Bandwidth",
"33. Wired not Wireless",
"34. Compression of Large Transfer Payloads",
"35. Persistent Connections",
"36. Connection Pools",
"37. UDP not TCP",
"38. Minimize Chattiness of Comm Protocols",
"39. Pass Smaller Messages",
"40. Make Use of Otherwise Unused Local GPU For General/Parallel Compute Tasks",
"41. Make Use of Cloud Computing Services (eg. AWS)",
"42. Tuning OS Parameters",
"43. Custom OS Kernel Builds",
"44. Non-Virtual OS Instance",
"45. RTOS (if require a guarantee & hard upper bound on latency of action in response to event)",
"46. No OS (yes extreme but consider case of micro-controller where only 1 master program req)",
"47. Pass and Store Diffs Rather Than Complete Snapshots",
"48. Client-Server Architecture (eg. benefit: long startup init tasks done in server not clients)",
"49. Push Work To Client-Side Rather Than Server-Side (eg. rendering, initial input validation)",
"50. Local Function Calls Rather Than RPC or Web Service Requests",
"51. Function Memoization",
"52. Function Inlining",
"53. Loop Unrolling",
"54. Less Unnecessary Call Descent Depth (eg. Java/Enterprise Design Pattern Astronaut Arch)",
"55. Less Memory Churn and Background GC Inside Your Process",
"56. Object Pooling",
"57. Clusters",
"58. Queues with Worker Process/Thread Pools",
"59. Database Indexing",
"60. Database Stored Procedures",
"61. Database Prepared Statements",
"62. Database Sharding",
"63. Old Data Warehousing/Archiving",
"64. Old Metric/Event Rollups",
"65. Log Archiving",
"66. Timeout Guards",
"67. Buffer Size Tuning",
"68. Queue Size Tuning",
"69. Timeout Duration Tuning",
"70. Network Packet Size Tuning",
"71. Disk Page Size Tuning",
"72. Memory Page Size Tuning",
"73. Cache Size Tuning",
"74. Cache Eviction/Expiration Policy Tuning",
"75. Page Boundary Alignment Optimization",
"76. Powers of Two (other powers less efficient for memory addresses & sizes, with more waste)",
"77. Bit Packing (making every bit yield the maximum signal/use for the buck)",
"78. Run Bottleneck Processes with Max Priority, Minimum Niceness",
"79. Avoid Need To Mitigate Risk Of Hardware Failures Due To Vibration/Shock",
"80. Avoid Need To Mitigate Impact Of Environmental Radiation (eg. cosmic x-rays)",
"81. Reduce Physical Volume (eg. consider design impact on smartphones and data centers)",
"82. Reduce Physical Mass (eg. consider compute capabilities & cost impact on space payloads)",
"83. Reduce Power Consumption (eg. smartphones, laptop battery life, data centers)",
"84. Reduce Heat Emission (eg. impacts cooling reqs thus total cost/complexity of data centers)",
"85. Keep Hardware Cool, Especially Processors",
"86. Increase MTBF of Least Reliable Hardware Component",
"87. Commodity Priced Hardware Rather Than Vendor Monopoly/Patented/Unique Hardware",
"88. Later/Recent Generation Hardware Models (in general: more optimized than earlier/older)",
"89. Decrease Max/Mean/Min Time Before Detection of Failure",
"90. Upstream DoS Throttling/Filtering",
"91. User Request Throttling",
"92. Automatic Load Balancing (esp smarter)",
"93. Off-Peak Scheduling of Tasks When Possible",
"94. Encourage/Require Users To Spread Access/Requests/Workloads More Evenly Over Time",
"95. No Encryption",
"96. Minimize Core/Thread Context Switching",
"97. Avoid Mem/Disk Paging/Swapping, Especially Thrashing",
"98. Higher OS Scheduling Priority For Processes Directly Responding To Live User Commands",
"99. Avoid Lock Contention",
"100. Textual UI’s and CLI’s Rather Than GUI’s",
"101. Text Rather Than Images and Static Images Rather Than Video, Audio or Animations",
"102. Vector Illus/Anims/UI’s Rather Than Bitmaps To Minimize Disk/Net/Mem Footprint",
"103. JSON/CSV/etc Rather Than XML (whose impls often cause higher latency or mem use)",
"104. Prefer Precise, Reactive, Resource Sipping Tools (eg. lat/cpu/mem of vim over Eclipse)",
"105. Automated Rather Than Manual (eg. no content staff approval queue, just filter and flag)",
"106. Mass Viral Parasitic Disguised Idle Compute (eg. malware)",
"107. Humans For Tasks Where Cheaper, Faster, Most Accurate, Most Believable, Multi-Purpose",
"108. Quantum Computing (in theory; for certain problem types)",
"109. Make Light Speed in Vacuum Your Only Remaining Latency Bottleneck Where Possible",


"elastic microservices arch for greater scalability, resiliency",

"uniform distribution of tasks across a regular time window where possible (eg. say you have 100 servers which must be rebooted one per day (and a server reboot takes typically max of 2 minutes), you don’t reboot them all at the same moment, but spread them out evenly so never more than 1 server rebooting at any point during any 24 hour window) NOTE this is very close to existing #94 and 93",

"random jigging/jittering of attempt tries to avoid stampedes",

"assembly. inline ASM (like in C)",

"add some cloud, NN, ML and 'data science' specific items to candidate list, where distinction warrants",

"TODO some in my notes on phone?",

"speculative branch prediction (similar to 17 Precompute Predicted Requests)",

"probable bets (needs work; flesh out or drop this)",

"Bayesian inference",

"multi-modem or multi-ISP or multi-NIC or multi-route requests or downloading (blast multiple redundant requests in parallel down different pipes and see which one wins; or divide a requested large file into smaller pieces and fetch each in parallel from a separate path then reassemble on client's end once have all)",

"dedicated physical network routes (ie. what Google and Amazon likely do between their data centers)",

"mass coordination by clients/users to self-distribute target addresses and request times in a balance way (redund?)",

"JIT bytecode optimizations",

"in GUI, not rerender to pixels any faster than the display refresh cycle",

"in 3D UIs, view-model culling",

"image compression (to reduce bandwidth, boost throughput, reduce disk space footprint). add audio and video (similar to 34 Compression of Large Transfer Payloads; related to 102)",

"at runtime drop value checking guards (think asserts and null guards) to boost speed, if wont cause problems, or tradeoff on elavated error rate is acceptable",

"disable GC (I believe already have 'tune GC' in my list)",

"log output reducing (eg. via quieter levels) or total disabling/muting",

"log writes to faster write-turnaround target (even if ephemeral like memory)",

"no alloc function calls (so caller can reuse pre-allocated memory slabs, to reduce latency and better control lifecycle of memory objects) (maybe redund/overlap with existing 'object pools' item)",

"ensure no memory gets paged out to disk (via OS-wide disabling, or, by having the app workoad be very careful?) {related to 42 Tuning OS Params)",

"faked not real (eg. mocked-up screen flows in a demo, not working code yet)",

"that neat technique Carmack once tweeted about? (IIRC)",

"smaller IC chips (very speculative and may drop this; TBD cuz on one hand I see why latencies within-chip could be faster however may also be other physics/materials effects at that tiny scale which disrupt or push back in opposite direction)",

"more on 1 chip (instead of external GPU or NN compute; eg. SoC, Apple's M1) (can't believe it took me 3+ years to add this)",
]

if __name__ == "__main__":
	for i,item in enumerate(items):
		print("%i. %s" % (i+1,item))
