module task2_top (
	input  [9:0] SW,		// 10-bit input switches
	output [6:0] HEX0,	
	output [6:0] HEX1,	// hex output on 7-segment displays
	output [6:0] HEX2
);

hex_to_7seg SEG0 (		// instantiate hex_to_7seg for HEX0
	.in(SW[3:0]),
	.out(HEX0)
);

hex_to_7seg SEG1 (		// instantiate hex_to_7seg for HEX1
	.in(SW[7:4]),
	.out(HEX1)
);

hex_to_7seg SEG2 (		// instantiate hex_to_7seg for HEX2
	.in({2'b0, SW[9:8]}),
	.out(HEX2)
);

endmodule
