# Compte rendu — TD 3 : Génération procédurale de villes
*ESIEE – Année 2025-2026*  

## Principes de base

### Théorique
L’idée est de générer une ville automatiquement à partir d’une carte de valeurs, souvent un bruit comme le Perlin. Les zones où la valeur est élevée reçoivent des bâtiments plus grands, et les zones plus basses accueillent des petites maisons. Cette approche permet d’obtenir des quartiers cohérents sans placement manuel.

### Pratique
On réutilise la structure du terrain procédural, mais au lieu de modifier la hauteur du mesh, on instancie des bâtiments en fonction de la valeur Perlin.

```csharp
public class MakeCity : MonoBehaviour {
    public GameObject[] buildings;

    void Start() {
        Perlin p = new Perlin();
        Mesh m = GetComponent<MeshFilter>().mesh;
        Vector3[] verts = m.vertices;

        for(int i=0; i<verts.Length; i++) {
            float val = p.Noise(verts[i].x * 2f, verts[i].z * 2f) * 10f;
            int id = Mathf.Clamp(Mathf.RoundToInt(val), 0, buildings.Length - 1);

            Instantiate(buildings[id],
                new Vector3(verts[i].x, 0, verts[i].z),
                buildings[id].transform.rotation);
        }
    }
}