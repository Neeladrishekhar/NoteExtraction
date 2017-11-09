const scribble = require('scribbletune');
// var clip = scribble.clip({
//     notes: ['c#4'] ,
//     pattern: 'x' , // 1 sec for Qmmp player
//     // pattern: 'x_'.repeat(4*10) ,// 10 sec ... every beat is 1/8 th of a sec.
//     accentMap: [41]
//     // accentMap: [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 120, 120, 120] //[1..127]
// });
// scribble.midi(clip, 'data/one_note.mid');
// var clip = scribble.clip({
//     notes: ['c3'] ,
//     pattern: 'x'+'_'.repeat(7) , // 1 sec for Qmmp player
//     // pattern: 'x_'.repeat(4*10) ,// 10 sec ... every beat is 1/8 th of a sec.
//     accentMap: [41]
//     // accentMap: [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 120, 120, 120] //[1..127]
// });
// scribble.midi(clip, 'data/one_note3.mid');

// var scal = ['1', '2', '3', '4', '5', '6', '7', '8']
var base = ['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#']

for (var volume = 41; volume <= 120; volume++) { // volume of the note
	for (var scale = 1; scale <= 8; scale++) {	// scale of the note
		for (var j = 0; j < base.length; j++) {
			var clip = scribble.clip({
				notes: [base[j]+scale] ,
				pattern: 'x' ,
				accentMap: [volume]
			});
			scribble.midi(clip, 'data/'+base[j]+scale+'_'+volume+'.mid');
		}
	}
}