module task1_top (
	input   [3:0] SW,        // 4-bit input switches
	output  [6:0] HEX0       // hex output on 7-segment display
);

    // instantiate the hex_to_7seg module
    hex_to_7seg SEG0 (
        .in(SW[3:0]),
        .out(HEX0)
    );

endmodule