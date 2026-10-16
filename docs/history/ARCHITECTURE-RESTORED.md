# Architecture restored

The Python pipeline substitutes (`lang/hindawi/pipeline/`) have been removed.

The original architecture is:

native source → Flex .uhin → C → gcc

The .uhin files are Flex lexers. They require Flex to compile. Flex is not available in this environment.

Original Hindi .uhin files (unchanged):
- upstream/chintamani/guru/h2c.uhin
- upstream/chintamani/shraeni/h2cpp.uhin
- upstream/chintamani/soochee/h2py.uhin
- upstream/chintamani/praatha/h2b.uhin
- upstream/chintamani/wyaaka/h2yacc.uhin
- upstream/chintamani/shabda/h2l.uhin

Generated .uhin for Devanagari languages follow the same Flex structure.
