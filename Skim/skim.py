import ROOT

f = ROOT.TFile("../../hh4b-v00-00-00.root")
t = f.Get("XhhMiniNtuple")

def setInput(filename = ""):
	global f
	global t

	if filename == "":
		filename = "../../hh4b-v00-00-00.root"

	f = ROOT.TFile(filename)
	t = f.Get("XhhMiniNtuple")

	print "Setting input to be %s ..." % (filename)

def skim(selection, filename):
	print "Begin to skim wth selection: %s" % (selection)
	
	fnew = ROOT.TFile(filename, "RECREATE")
	tnew = t.CopyTree(selection)
	fnew.WriteTObject(tnew, tnew.GetName(), "Overwrite")

	print "Finish skimming. Output is in %s" % (filename)

def test():
	# setInput("../../RSG.root")
	# skim("PassBoosted == 1", "RSG_boosted.root")

	setInput("RSG_boosted.root")
	skim("(PassLeadJetPt == 1) && (PassSubLeadJetPt == 1)", "RSG_boosted_PassLeadSubLeadJetPt.root")