const scribble = require('scribbletune');

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